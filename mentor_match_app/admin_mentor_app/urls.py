from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='login'),
    path("register/", views.register, name="register"),
    #  Dashboard
    path("", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    # Mentees accept_mentee
    path("my-mentees/", views.get_mentees, name="mentees"),
    path( "preview_mentee/<int:mentee_id>/", views.preview_mentee, name="preview_mentee"),
    path( "accept_mentee/<int:match_id>/", views.accept_mentee, name="accept_mentee"),
    path( "reject_mentee/<int:match_id>/", views.reject_mentee, name="reject_mentee"),
    # send_message
    path("send_message/", views.send_message, name="send_message"),
    
    # Update Goals
    path("update_goal_status/", views.update_goal_status, name="update_goal_status"),
    path("delete_goal/", views.delete_goal, name="delete_goal"),
    path("add_goal/", views.add_goal, name="add_goal"),
    
    # schedule
    path("schedule/", views.schedule, name="schedule"),
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
    path('evaluation_form/', views.evaluation_form, name='evaluation_form'),
    path('answered_form/<str:firstname>/', views.answered_form, name='answered_form'),
    path('answers', views.answers, name='answers'),
    path('thank_you/', views.thank_you, name='thank_you'),

    # reports
    path("reports/", views.reports, name="reports"),
    
    
]
