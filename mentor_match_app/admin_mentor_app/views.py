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

#evaluation
def calculate_progress_for_all(request):
    mentee_ids = []
    # Retrieve all unique mentee_ids from Progress
    mentor_id = request.user.id

# Get distinct mentee_ids where mentor_id equals the current logged-in user's ID
 # Get the current logged-in user's ID
    mentee_ids = Progress.objects.filter(mentorId=mentor_id).values_list('mentee_id', flat=True).distinct()

    mentee_progress = []

    for mentee_id in mentee_ids:
        # Count distinct goals for each mentee_id
        total_goals = Progress.objects.filter(mentee_id=mentee_id).values('goal').distinct().count()
        completed_goals = Progress.objects.filter(mentee_id=mentee_id, status='complete').values('goal').distinct().count()

        # Calculate the percentage of completed goals
        if total_goals > 0:
            percentage = (completed_goals / total_goals) * 100
        else:
            percentage = 0

        # Add to list if the percentage is 100
        if percentage == 100:
            mentee_progress.append(mentee_id)

    return mentee_progress

def evaluation(request):
    # Get mentees with 100% progress
    mentees_with_100_percent = calculate_progress_for_all(request)

    if mentees_with_100_percent:
        # Get user details from the User model for mentees with 100% progress
        users = User.objects.filter(
            id__in=mentees_with_100_percent
        ).values('first_name', 'last_name', 'email')
    else:
        users = []

    # Render the evaluation template with the user details
    return render(request, "admin_mentor_app/evaluation/evaluation.html", {'users': users})

# Evaluation form

def evaluation1(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = Evaluation(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                support=form.cleaned_data.get('support')[0],
                communication=form.cleaned_data.get('communication')[0],
                confidence=form.cleaned_data.get('confidence')[0],
                career=form.cleaned_data.get('career')[0],
                understanding=form.cleaned_data.get('understanding')[0],
                comfort=form.cleaned_data.get('comfort')[0],
                goals=form.cleaned_data.get('goals')[0],
                recommend=form.cleaned_data.get('recommend')[0],
                resources=form.cleaned_data.get('resources')[0],
                additional_resources=form.cleaned_data.get('additional_resources', ''),
                additional_comments=form.cleaned_data.get('additional_comments', '')
            )
            evaluation.save()
            return HttpResponse("Thank you for your feedback!")
    else:
        form = EvaluationForm()

    return render(request, 'admin_mentor_app/evaluation/evaluation_form.html', {'form': form})
    return render(request, 'admin_mentor_app/evaluation/evaluation_form.html', {'form': form})

def form(request):
    return render(request, "admin_mentor_app/evalution/thanks.html")
def evaluation_list(request):
    first_name = request.GET.get('first_name')
    evaluation = None
    
    if first_name:
        evaluations = Evaluation.objects.filter(first_name=first_name)
        if evaluations.exists():
            evaluation = evaluations.first()
        else:
            return HttpResponse("No evaluation found for this user.")

    return render(request, 'admin_mentor_app/evaluation/evaluation_list.html', {
        'evaluation': evaluation
    })

 