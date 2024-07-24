from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, UserRegisterForm



def logout_view(request):
    auth_logout(request)
    return redirect('login')
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to a success page.
                # if user.role==1 or user.role==2:
                return redirect('dashboard')
                
                    
                
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'admin_mentor_app/login.html', {'form': form})

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

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)  # Login the user
#                 return redirect('dashboard')  # Redirect to dashboard or desired page
#             else:
#                 # Invalid login credentials
#                 form.add_error(None, "Invalid username or password.")
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', context={'form': form})



# def register(request):
#     form = UserRegisterForm()
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             form.save()
#             return redirect('login')
           
#     else:
#         form = UserRegisterForm()
#     return render(request, 'admin_mentor_app/register.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    return render(request, "admin_mentor_app/dashboard/dashboard.html")

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
    return render(request, 'admin_mentor_app/reports/reports.html', {'chart_paths': chart_paths})