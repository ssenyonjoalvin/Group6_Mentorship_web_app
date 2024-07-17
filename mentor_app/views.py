from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
   return render(request,'mentor_app/index.html')

def register(request):
   if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('registration_success')
   else:
        form = UserRegistrationForm()

   return render(request, 'mentor_app/register.html', {'form': form})
   # return render(request,'mentor_app/register.html')

def choice_user_type(request):
   return render(request,'mentor_app/choice_user_type.html')