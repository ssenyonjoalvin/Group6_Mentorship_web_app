from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Login the user
                return redirect('dashboard')  # Redirect to dashboard or desired page
            else:
                # Invalid login credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})



def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
           
    else:
        form = UserRegisterForm()
    return render(request, 'admin_mentor_app/register.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    return render(request, "admin_mentor_app/dashboard/dashboard.html")

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
