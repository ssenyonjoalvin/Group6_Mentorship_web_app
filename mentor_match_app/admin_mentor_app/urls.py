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
    path('edit_appointment/', views.edit_appointment, name='edit_appointment'),
    path('mark_complete/<int:schedule_id>/', views.mark_complete, name='mark_complete'),
    path('delete_appointment/<int:schedule_id>/', views.delete_appointment, name='delete_appointment'),
    path('schedule_list/', views.schedule_list, name='schedule_list'),
    # evaluation
    path('evaluation/', views.evaluation, name='evaluation'),

    # reports
    path('reports/', views.reports, name='reports'),
    
    

    ]