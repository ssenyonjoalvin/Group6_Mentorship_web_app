
from django.urls import path
from . import views

app_name = 'mentees_app'

urlpatterns = [
    path('home/', views.mentee_home, name='mentee_home'),

    # find mentor
    path('find-mentor/', views.find_mentor, name='find_mentor'),
]
