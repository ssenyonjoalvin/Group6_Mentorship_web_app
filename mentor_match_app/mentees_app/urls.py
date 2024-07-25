from django.urls import path
from . import views

app_name = 'mentees_app'

urlpatterns = [
    path('home/', views.mentee_home, name='mentee_home'),
    path('find_mentor/', views.find_mentor, name='find_mentor'),
    path('messages/', views.mentee_messages, name='messages'),
    path('api/chats/<int:chat_id>/', views.get_chat_details, name='get_chat_details'),
    path('profile/', views.mentee_profile, name='profile'),
    path('programs/', views.mentee_programs, name='programs'),
    path('resources/', views.mentee_resources, name='resources'),
]
