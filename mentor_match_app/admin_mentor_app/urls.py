from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='login'),

    path('register/', views.register, name='register'),

    #  Dashboard
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

    # Mentees
    path('my-mentees/', views.get_mentees, name='mentees'),
    path('preview_mentee/<int:mentee_id>/', views.preview_mentee, name='preview_mentee'),
    # send_message
    path('send_message/', views.send_message, name='send_message'),


     
     #se
    #schedule
    path('schedule/', views.schedule, name='schedule'),

    # evaluation
    path('evaluation/', views.evaluation, name='evaluation'),

    # reports
    path('reports/', views.reports, name='reports'),
    
    

    ]