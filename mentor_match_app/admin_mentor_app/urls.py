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
    # path('evaluation1/', views.evaluation1, name='evaluation1'),
    # path('evaluation2', views.evaluation_list, name='evaluation_list'),

    # reports
    path('reports/', views.reports, name='reports'),
    
     # reports
    path('notifications/', views.notifications, name='notifications'),
    ]