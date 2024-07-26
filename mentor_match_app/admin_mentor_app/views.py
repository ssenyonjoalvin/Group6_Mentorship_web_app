from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from urllib import request
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, UserRegisterForm,ProfileUpdateForm,EditAppointmentForm
import matplotlib
from django.db import transaction, connection
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
import pytz
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from .models import (
    User,
    MentorshipMatch,
    Message,
    Notification,
    Schedule,
    Progress,
    Goals,
    Evaluation,
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
                auth_login(request, user)
                return redirect("dashboard")
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
        my_mentees = MentorshipMatch.objects.raw("SELECT * FROM admin_mentor_app_mentorshipmatch where mentor_id=1")
        mentor_mentees_ids = []
        for my_mentee in my_mentees:
            mentor_mentees_ids.append(my_mentee.mentee.id)
            print(mentor_mentees_ids)
            
        print(mentor_mentees_ids)
        mentees = []
        for mentor_mentees_id in mentor_mentees_ids:
            mentee = User.objects.get(id=mentor_mentees_id)
            mentees.append(mentee)
        print(mentees)
        my_mentees=mentees

        return render(request, "admin_mentor_app/mentee/get_mentees.html", {'my_mentees': my_mentees})
    finally:
        connection.close()
@login_required
@transaction.atomic
def preview_mentee(request, mentee_id):
    try:
        logged_in_user = request.user.id
        mentee = get_object_or_404(User, id=mentee_id)

        # Get messages between logged_in_user and mentee
        messages = Message.objects.filter(
            (Q(sender_id=logged_in_user) & Q(receiver_id=mentee_id)) |
            (Q(sender_id=mentee_id) & Q(receiver_id=logged_in_user))
        ).order_by('sent_at')  # Order messages by sent time

        return render(request, 'admin_mentor_app/mentee/preview_mentee.html', {
            'mentee': mentee,
            'messages': messages
        })
    finally:
        connection.close()

@method_decorator(csrf_exempt, name='dispatch')
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        file = request.FILES.get('file') if 'file' in request.FILES else None
        receiver_id = request.POST.get('receiver_id')
        sender_id = request.user.id
        
        print(content)
        receiver = User.objects.get(id=receiver_id)
        sent_at = datetime.datetime.now()
        
        message = Message.objects.create(
            receiver_id=receiver_id,
            sender_id=sender_id,
            content=content,
            file=file,
            sent_at=sent_at
        )
        if message:
            print("Saved")
        
        return JsonResponse({'status': 'success', 'message': 'Message sent successfully.'})
    return JsonResponse({'status': 'failure', 'message': 'Invalid request.'})
# Schedule view
@csrf_exempt
@login_required
def schedule(request):
    if request.method == 'GET':
        # Handle GET request: render the schedule page with the list of users
        # Get the ID of the logged-in mentor
        loggedinmentor = request.user.id

        # Fetch all schedules for the logged-in mentor with prefetching mentees
        schedules = Schedule.objects.filter(mentor_id=loggedinmentor).select_related('mentee')

        # Create a list of dictionaries with mentee details and corresponding schedule
        schedule_list = [
            {
                'mentee': schedule.mentee,
                'schedule': schedule
            }
            for schedule in schedules
        ]

        # Print the optimized schedule list
        print(schedule_list)

        return render(request, "admin_mentor_app/schedule/schedule.html", {'schedule_list': schedule_list})

    
    if request.method == 'POST':
        # Retrieve form data 
        mentor_id = request.POST.get('mentee_id')
        scheduleId = request.POST.get('scheduleId')
        mentee_id = request.POST.get('mentee_id_row')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')

        # Combine date and time into a single datetime object
        appointment_datetime_str = f"{appointment_date}T{appointment_time}:00"
        appointment_datetime = parse_datetime(appointment_datetime_str)

    

        # Define the status
        status = "scheduled"

        # Update or create the schedule appointment
        # Update or create the schedule appointment
        Schedule.objects.update_or_create(
            mentor_id=mentor_id,
            mentee_id=mentee_id,
            id=scheduleId,
            defaults={
                'session_date': appointment_datetime,
                'status': status
            }
        )

        

        # Redirect to the schedule page
        return redirect('schedule')  # Make sure 'schedule' is the name of the 

    # Handle other request methods
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
@login_required
@require_http_methods(['GET'])
def mark_complete(request, schedule_id):
    try:
        schedule = get_object_or_404(Schedule, id=schedule_id)
        schedule.status = 'completed'
        schedule.save()

 # Redirect to the schedule page
        return redirect('schedule')  # Make sure 'schedule' is the name of the 

    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    


@require_POST
@login_required
def delete_appointment(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    
    # Check if the current user is authorized to delete this schedule
    if request.user.id != schedule.mentor_id:
        return HttpResponseForbidden("You are not authorized to delete this appointment.")
    
    schedule.delete()
    
    return redirect('schedule')  


@login_required
def schedule_list(request):
    status_filter = request.GET.get('status', 'all')

    if status_filter == 'all':
        schedule_list = Schedule.objects.filter(mentor_id=request.user.id)
    else:
        schedule_list = Schedule.objects.filter(
            mentor_id=request.user.id,
            status=status_filter.lower()  # Adjust based on your status field
        )

    if request.is_ajax():  # Check if the request is an AJAX request
        data = {'schedule_list': [{'name': schedule.name, 'status': schedule.status} for schedule in schedule_list]}
        return JsonResponse(data)
    else:
        return render(request, 'schedule.html', {'schedule_list': schedule_list})
@csrf_exempt
@login_required
def edit_appointment(request):
    if request.method == 'POST':
        form = EditAppointmentForm(request.POST)
        if form.is_valid():
            mentee_id = request.POST.get('mentee_id')
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']
            
            appointment_datetime_str = f"{appointment_date}T{appointment_time}:00"
            appointment_datetime = parse_datetime(appointment_datetime_str)

            # Update the schedule
            schedule = get_object_or_404(Schedule, mentee_id=mentee_id)
            schedule.session_date = appointment_datetime
            schedule.status = 'scheduled'
            schedule.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form is invalid'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
# Evaluation
@login_required
@transaction.atomic
def evaluation(request):
    try:
        return render(request, "admin_mentor_app/evaluation/evaluation.html")
    finally:
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
