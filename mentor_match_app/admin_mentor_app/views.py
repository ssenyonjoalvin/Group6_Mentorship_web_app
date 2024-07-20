from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "admin_mentor_app/login.html")

def register(request):
    return render(request, "admin_mentor_app/register.html")

# Dashboard
def dashboard(request):
    return render(request, "admin_mentor_app/dashboard/dashboard.html")

# Mentee
def get_mentees(request):
    return render(request, "admin_mentor_app/mentee/get_mentees.html")

def preview_mentees(request):
    return render(request, "admin_mentor_app/mentee/preview_mentees.html")

#schedule
def schedule(request):
    return render(request, "admin_mentor_app/schedule/schedule.html")

#evaluation

def evaluation(request):
    return render(request, "admin_mentor_app/evaluation/evaluation.html")

