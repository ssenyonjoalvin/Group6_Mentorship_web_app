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
    path('preview-mentee/', views.preview_mentees, name='preview_mentee'),
     
     #se
    #schedule
    path('schedule/', views.schedule, name='schedule'),

    # evaluation
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluation_form/', views.evaluation_form, name='evaluation_form'),
    path('answered_form/<str:firstname>/', views.answered_form, name='answered_form'),
    path('answers', views.answers, name='answers'),
    path('thank_you/', views.thank_you, name='thank_you'),

    # reports
    path('reports/', views.reports, name='reports'),
    
     # reports
    path('notifications/', views.notifications, name='notifications'),
    ]