from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from urllib import request
from django.db.models import Q
import math
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, UserRegisterForm

from .forms import LoginForm, UserRegisterForm,ProfileUpdateForm
import matplotlib
from django.db import transaction, connection
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings
from django import db
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
import pytz
from django.http import JsonResponse
from .models import (
    User,
    MentorshipMatch,
    Message,
    Notification,
    Schedule,
    Progress,
    Goals,
    Evaluation,
    MenteeChallenge
)


def logout_view(request):
    auth_logout(request)
    return redirect("login")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                print(user)
                auth_login(request, user)
                print(f"User role: {user.role}")  # Debug print

                if user.role == '2':
                    return redirect("dashboard")                    
                elif user.role == '3':
                    return redirect("mentees_app:mentee_home")
                else:
                    print(f"Unknown role: {user.role}")  # Debug print
                
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "admin_mentor_app/login.html", {"form": form})

def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "admin_mentor_app/register.html", {"form": form})

@login_required
@transaction.atomic
def dashboard(request):
    try:
        unread_notifications = Notification.objects.count()
        total_progress_count = Progress.objects.count()
        schedules = Schedule.objects.all()
        completed_count = Progress.objects.filter(progress_percentage="100%").count()
        pending_count = total_progress_count - completed_count
        users = User.objects.all()
        progresses = Progress.objects.all()
        print(pending_count)

        return render(
            request,
            "admin_mentor_app/dashboard/dashboard.html",
            {
                "global_progress": progresses,
                "completed": completed_count,
                "pending_count": pending_count,
                "total_progress_count": total_progress_count,
                "users": users,
                "schedules": schedules,
                "unread_notifications": unread_notifications,
            },
        )
    finally:
        db.connections.close_all()
        connection.close()
@login_required        
def profile(request):
    user = request.user  # Get the currently logged-in user
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, "admin_mentor_app/dashboard/profile.html", {"form": form})

@login_required
@transaction.atomic
def get_mentees(request):
    try:
        mentor_id = request.user.id
        # Fetch all MentorshipMatch records for the given mentor
        mentorship_matches = MentorshipMatch.objects.filter(mentor_id=mentor_id).select_related('mentee')

        # Extract mentee objects and mentorship match records
        mentees_with_matches = []
        for match in mentorship_matches:
            mentees_with_matches.append({
                'mentee': match.mentee,
                'match': match
            })

        return render(request, "admin_mentor_app/mentee/get_mentees.html", {'mentees_with_matches': mentees_with_matches})
    finally:
        connection.close()
@login_required
@transaction.atomic
def accept_mentee(request, match_id):
    mentorship_match = get_object_or_404(MentorshipMatch, id=match_id)
    mentorship_match.status = 'accepted'
    mentorship_match.save()
    return redirect('mentees')

@login_required
@transaction.atomic
def reject_mentee(request, match_id):
    mentorship_match = get_object_or_404(MentorshipMatch, id=match_id)
    mentorship_match.status = 'rejected'
    mentorship_match.save()
    return redirect('mentees')
    
             
@login_required
@transaction.atomic
def preview_mentee(request, mentee_id):
    logged_in_user = request.user.id
    mentee = get_object_or_404(User, id=mentee_id)
    
    messages = Message.objects.filter(
        (Q(sender_id=logged_in_user) & Q(receiver_id=mentee_id)) |
        (Q(sender_id=mentee_id) & Q(receiver_id=logged_in_user))
    ).order_by('sent_at')  # Order messages by sent time
    
    menteechallenges = MenteeChallenge.objects.filter(
        mentee_id=mentee_id,
        mentor_id=logged_in_user
    )

    mentor_progress_groups = Progress.objects.filter(
        mentee_id=mentee_id,
        mentor_id=logged_in_user
    )
    
    progresses = []
    for mentor_progress in mentor_progress_groups:
        goals = Goals.objects.filter(
            goal_id=mentor_progress
        )
        progresses.append({
            'session_number': mentor_progress.session_number,
            'progress_percentage': mentor_progress.progress_percentage,
            'goals': goals,
            # 'status': goals.status
        })

    return render(request, 'admin_mentor_app/mentee/preview_mentee.html', {
        'mentee': mentee,
        'messages': messages,
        'menteechallenges': menteechallenges,
        'progresses': progresses
    })

@csrf_exempt
@require_POST
def add_goal(request):
    goal_text = request.POST.get('newGoal')
    progress_id = request.POST.get('progress_id')
    
    try:
        progress = Progress.objects.get(session_number=progress_id)
        new_goal = Goals.objects.create(
            goal_id=progress,
            goal=goal_text,
            status='Pending'
        )
        new_goal.save()

        # Calculate the progress percentage
        total_goals = progress.session_goals.count()
        completed_goals = progress.session_goals.filter(status='Completed').count()
        
        if total_goals == 0:
            progress_percentage = 0
        else:
            progress_percentage = (completed_goals / total_goals) * 100
        
        progress.progress_percentage = str(math.floor(progress_percentage))
        progress.save()

        return JsonResponse({'success': True, 'goal': {
            'id': new_goal.id,
            'goal': new_goal.goal,
            'status': new_goal.status
        }})
    except Progress.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Progress not found'})@method_decorator(csrf_exempt, name='dispatch')
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        file = request.FILES.get('file') if 'file' in request.FILES else None
        receiver_id = request.POST.get('receiver_id')
        sender_id = request.user.id
        
        print(content)
        receiver = User.objects.get(id=receiver_id)
        sent_at = datetime.datetime.now()
        
        message = Message(
            receiver_id=receiver_id,
            sender_id=sender_id,
            content=content,
            file=file,
            sent_at=sent_at
        )
        if message.save():      
            print("Saved")
        
        return JsonResponse({'status': 'success', 'message': 'Message sent successfully.'})
    return JsonResponse({'status': 'failure', 'message': 'Invalid request.'})

@require_POST
def update_goal_status(request):
    goal_id = request.POST.get('goal_id')
    status = request.POST.get('status')
    
    try:
        goal = Goals.objects.get(id=goal_id)
        goal.status = status
        goal.save()

        # Calculate the progress percentage
        progress = goal.goal_id
        total_goals = progress.session_goals.count()
        completed_goals = progress.session_goals.filter(status='Completed').count()
        
        if total_goals == 0:
            progress_percentage = 0
        else:
            progress_percentage = (completed_goals / total_goals) * 100
        
        progress.progress_percentage = str(math.floor(progress_percentage))
        progress.save()

        return JsonResponse({'success': True})
    except Goals.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Goal not found'})
@require_POST
def delete_goal(request):
    goal_id = request.POST.get('goal_id')
    
    try:
        goal = Goals.objects.get(id=goal_id)
        goal.delete()
        return JsonResponse({'success': True})
    except Goals.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Goal not found'})

@login_required
@transaction.atomic
def schedule(request):
    if request.method == 'GET':
        # Handle GET request: render the schedule page with the list of users
        schedule_list = User.objects.all()
        return render(request, "admin_mentor_app/schedule/schedule.html", {'schedule_list': schedule_list})

    elif request.method == 'POST':
        # Handle POST request: process the form submission for scheduling
        mentee_id = request.POST.get('mentee_id')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')

        # Combine date and time into a single datetime object
        appointment_datetime_str = f"{appointment_date}T{appointment_time}:00"
        appointment_datetime = parse_datetime(appointment_datetime_str)

        # Ensure the datetime is timezone-aware
        if appointment_datetime is not None:
            appointment_datetime = make_aware(appointment_datetime, timezone=pytz.UTC)

        # Find the relevant mentee and create/update the Schedule instance
        try:
            mentee = User.objects.get(id=mentee_id)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Mentee not found'})

        # Check if there's already an existing schedule for this mentee
        schedule, created = Schedule.objects.update_or_create(
            mentee=mentee,
            defaults={
                'session_date': appointment_datetime,
                'status': 'scheduled'  # Update status as needed
            }
        )

        return JsonResponse({'status': 'success'})

    # Handle other request methods
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

 
# Evaluation
@login_required
@transaction.atomic
def evaluation(request):
    try:
        return render(request, "admin_mentor_app/evaluation/evaluation.html")
    finally:
        db.connections.close_all()
        connection.close()

def generate_charts():
    try:
        matplotlib.use('Agg')
        static_directory = os.path.join(settings.BASE_DIR, 'static/admin_mentor_app/charts')
        os.makedirs(static_directory, exist_ok=True)

        mentees_per_month = [5, 10, 15, 20, 25, 30]
        months = ['January', 'February', 'March', 'April', 'May', 'June']

        progress_data = [10, 5, 15, 20]
        statuses = ['In Progress', 'Completed', 'On Hold', 'Dropped']

        plt.figure(figsize=(5, 4))
        sns.barplot(x=months, y=mentees_per_month)
        plt.title('Number of Mentees per Month')
        plt.tight_layout()
        histogram_path = os.path.join(static_directory, 'mentees_per_month.png')
        plt.savefig(histogram_path)
        plt.close()

        plt.figure(figsize=(5, 4))
        sns.barplot(x=statuses, y=progress_data)
        plt.title('Status and Progress of Mentees')
        plt.tight_layout()
        bargraph_path = os.path.join(static_directory, 'progress.png')
        plt.savefig(bargraph_path)
        plt.close()

        return {
            'histogram_path': 'admin_mentor_app/charts/mentees_per_month.png',
            'bargraph_path': 'admin_mentor_app/charts/progress.png',
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def reports(request):
    chart_paths = generate_charts()
    return render(request, 'admin_mentor_app/reports/reports.html', {'chart_paths': chart_paths})
