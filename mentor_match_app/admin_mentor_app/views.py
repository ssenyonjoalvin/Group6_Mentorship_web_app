from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, UserRegisterForm
from django.core.exceptions import ObjectDoesNotExist
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


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to a success page.
                # if user.role==1 or user.role==2:
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


# Dashboard
@login_required
def dashboard(request):
    unread_notifications = Notification.objects.count()
    # unread_notifications = Notification.objects.raw('SELECT *, count(*) as count FROM admin_mentor_app_notification where is_read =0')
    total_progress_count = Progress.objects.count()
    schedules = Schedule.objects.all()

    # Count of Progress records with progress_percentage equal to 100
    completed_count = Progress.objects.all().filter(progress_percentage="100%").count()
    pendind_count = (
        Progress.objects.all().count()
        - Progress.objects.all().filter(progress_percentage="100%").count()
    )
    users = User.objects.all()
    progresses = Progress.objects.all()
    print(unread_notifications)
    # for unread_notification in unread_notifications:
    #     print(unread_notification.message)

    return render(
        request,
        "admin_mentor_app/dashboard/dashboard.html",
        {
            "global_progress": progresses,
            "completed": completed_count,
            "pendind_count": pendind_count,
            "total_progress_count": total_progress_count,
            "users": users,
            "schedules": schedules,
            'unread_notifications':unread_notifications
        },
    )


def profile(request):
    return render(request, "admin_mentor_app/dashboard/profile.html")


# Mentee
@login_required
def get_mentees(request):
    mentor_id = request.user.id 
    my_mentees = MentorshipMatch.objects.raw("select * from admin_mentor_app_mentorshipmatch")
    
   
    return render(request, "admin_mentor_app/mentee/get_mentees.html", {'my_mentees':my_mentees})


def preview_mentees(request):
    return render(request, "admin_mentor_app/mentee/preview_mentees.html")


# Schedule
@login_required
def schedule(request):
    return render(request, "admin_mentor_app/schedule/schedule.html")


# Evaluation
@login_required
def evaluation(request):
    mentor_id = 9  # request.user.id
    progress = Progress.objects.filter(mentor_id=mentor_id).values('mentee_id').distinct()
    
    mentee_progress_list = []

    for record in progress:
        mentee_id = record['mentee_id']
        progress_percentage = Progress.objects.filter(mentor_id=mentor_id, mentee_id=mentee_id).values('progress_percentage').last().get('progress_percentage')
        
        mentee = User.objects.get(id=mentee_id)
        first_name = mentee.first_name
        last_name = mentee.last_name
        
        mentee_progress = {
            'mentee_id': mentee_id,
            'first_name': first_name,
            'last_name': last_name,
            'progress_percentage': progress_percentage
        }
        
        mentee_progress_list.append(mentee_progress)
            
    return render(request, 'admin_mentor_app/evaluation/evaluation.html', {'mentees': mentee_progress_list})

#EvaluationForm
@login_required
def evaluation_form(request):
    return render(request, 'admin_mentor_app/evaluation/evaluation_form.html')

def answers(request):
    if request.method == 'POST':
        
        evaluation = Evaluation(
            support=request.POST.get('support'),
            communication=request.POST.get('communication'),
            confidence=request.POST.get('confidence'),
            career=request.POST.get('career'),
            understanding=request.POST.get('understanding'),
            comfort=request.POST.get('comfort'),
            goals=request.POST.get('goals'),
            recommend=request.POST.get('recommend'),
            resources=request.POST.get('resources'),
            comments=request.POST.get('comments'),  # Consolidated comments field
            mentee_id=2,
            mentor_id=3,
            mentorship_match_id=4
            # Set the `mentor`, `mentee`, and `mentorship_match` fields as needed
        )
        evaluation.save()
        return redirect('thank_you')  # Redirect to the thank you view
    return render(request, 'admin_mentor_app/evaluation/evaluation_form.html')
def thank_you(request):
    return render(request, 'admin_mentor_app/evaluation/thanks.html')
@login_required
def reports(request):
    chart_paths = generate_charts()
    return render(
        request, "admin_mentor_app/reports/reports.html", {"chart_paths": chart_paths}
    )
def notifications(request):
    return render(request,"admin_mentor_app/notifications.html",{"notifications":notifications})

#Answered form
def get_mentee_id_by_firstname(firstname):
    try:
        # Retrieve the User object with the given firstname
        user = User.objects.get(first_name=firstname)
        return user.id
    except ObjectDoesNotExist:
        # Handle the case where the User with the given firstname does not exist
        return None

@login_required
def answered_form(request, firstname):
    # Get mentee_id using the firstname
    mentee_id = get_mentee_id_by_firstname(firstname)
    mentor_id = request.user.id

    if mentee_id is None:
        # Handle the case where the mentee_id was not found
        return render(request, 'admin_mentor_app/evaluation/error.html', {'message': 'Mentee not found.'})
        
    # Filter evaluations based on the mentee_id
    # mentor_id=3
    evaluations = Evaluation.objects.filter(mentee_id=mentee_id, mentor_id=mentor_id)

    if request.method == 'POST':
        for evaluation in evaluations:
            evaluation.support = request.POST.get(f'support_{evaluation.id}')
            evaluation.communication = request.POST.get(f'communication_{evaluation.id}')
            evaluation.confidence = request.POST.get(f'confidence_{evaluation.id}')
            evaluation.career = request.POST.get(f'career_{evaluation.id}')
            evaluation.understanding = request.POST.get(f'understanding_{evaluation.id}')
            evaluation.comfort = request.POST.get(f'comfort_{evaluation.id}')
            evaluation.goals = request.POST.get(f'goals_{evaluation.id}')
            evaluation.recommend = request.POST.get(f'recommend_{evaluation.id}')
            evaluation.resources = request.POST.get(f'resources_{evaluation.id}')
            evaluation.comments = request.POST.get(f'comments_{evaluation.id}')
            evaluation.save()  # Save each evaluation
            
        return redirect('thank_you')  # Adjust the redirect URL as needed

    return render(request, 'admin_mentor_app/evaluation/answered_form.html', {'evaluations': evaluations})