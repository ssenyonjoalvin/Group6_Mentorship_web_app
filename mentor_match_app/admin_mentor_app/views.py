from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, UserRegisterForm
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
    print(schedules)

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
        },
    )


def profile(request):
    return render(request, "admin_mentor_app/dashboard/profile.html")


# Mentee
@login_required
def get_mentees(request):
    return render(request, "admin_mentor_app/mentee/get_mentees.html")


def preview_mentees(request):
    return render(request, "admin_mentor_app/mentee/preview_mentees.html")


# Schedule
@login_required
def schedule(request):
    return render(request, "admin_mentor_app/schedule/schedule.html")


# Evaluation
@login_required
def evaluation(request):
    return render(request, "admin_mentor_app/evaluation/evaluation.html")


@login_required
def reports(request):
    chart_paths = generate_charts()
    return render(
        request, "admin_mentor_app/reports/reports.html", {"chart_paths": chart_paths}
    )
