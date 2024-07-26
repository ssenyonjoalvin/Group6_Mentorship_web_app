from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='login'),

    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),

    #  Dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor-dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('mentee-dashboard/', views.mentee_dashboard, name='mentee_dashboard'),

    path('profile/', views.profile, name='profile'),

    # Mentees
    path('my-mentees/', views.get_mentees, name='mentees'),
    path('preview-mentee/', views.preview_mentees, name='preview_mentee'),
     
     #se
    #schedule
    path('schedule/', views.schedule, name='schedule'),

    # evaluation
    path('evaluation/', views.evaluation, name='evaluation'),

    # reports
    path('reports/', views.reports, name='reports'),
    
    
    ]