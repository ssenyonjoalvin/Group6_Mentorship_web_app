from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
     path('register/', views.register, name='register'),

    #  Dashboard
     path('dashboard/', views.dashboard, name='dashboard'),

    # Mentees
     path('my-mentees/', views.get_mentees, name='mentees'),
     path('preview-mentee/', views.preview_mentees, name='preview_mentee'),
     
     #se
    #schedule
    path('schedule/', views.schedule, name='schedule'),

    # evaluation
    path('evaluation/', views.evaluation, name='evaluation'),
    
    
    ]