from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, UserRegisterForm
import matplotlib
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
import matplotlib.pyplot as plt
import seaborn as sns
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
    return render(request, "admin_mentor_app/evaluation/evaluation.html")

# Generate charts for the reports page
def generate_charts():

    try:
        # Use 'Agg' backend for Matplotlib
        matplotlib.use('Agg')

        # create static directory if it doesn't exist
        static_directory = os.path.join(settings.BASE_DIR, 'static/admin_mentor_app/charts')
        os.makedirs(static_directory, exist_ok=True)

        # sample data for charts
        mentees_per_month = [5, 10, 15, 20, 25, 30]
        months = ['January', 'February', 'March', 'April', 'May', 'June']

        progress_data = [10, 5, 15, 20]
        statuses = ['In Progress', 'Completed', 'On Hold', 'Dropped']

        # Histogram for Number of Mentees per Month
        plt.figure(figsize=(5, 4))
        sns.barplot(x=months, y=mentees_per_month)
        plt.title('Number of Mentees per Month')
        plt.tight_layout()  # Ensure the layout fits well
        histogram_path = os.path.join(static_directory, 'mentees_per_month.png')
        plt.savefig(histogram_path)
        plt.close()

        # Bar Graph for Status and Progress
        plt.figure(figsize=(5, 4))
        sns.barplot(x=statuses, y=progress_data)
        plt.title('Status and Progress of Mentees')
        plt.tight_layout()  # Ensure the layout fits well
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
