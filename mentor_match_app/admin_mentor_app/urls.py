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
    # evaluation
    path("evaluation/", views.evaluation, name="evaluation"),
    # reports
    path("reports/", views.reports, name="reports"),
    
    
]
