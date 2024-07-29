from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'mentees_app'

urlpatterns = [
    path('home/', views.mentee_home, name='mentee_home'),
    path('schedules/', views.schedules, name='schedules'),
    path('messages/', views.mentee_messages, name='messages'),
    path('api/chats/<int:chat_id>/', views.get_chat_details, name='get_chat_details'),
    path('send_request/', views.send_request, name='send_request'),
    path('profile/', views.mentee_profile, name='profile'),
    path('programs/', views.mentee_programs, name='programs'),
    path('resources/', views.mentee_resources, name='resources'),
    path('preview_mentor/<int:mentor_id>', views.previewMentor, name='previewMentor'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('cancel_appointment/<int:schedule_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('confirm_appointment/<int:schedule_id>/', views.confirm_appointment, name='confirm_appointment'),
    path('mentor/', views.mentor, name='mentor'),
    # path('evaluation_form/', views.evaluation_form, name='evaluation_form'),
    path('evaluation/form-fill/<int:mentor_id>', views.fillEvaluationForm, name='fillEvaluationForm'),
    path('evaluation/form-fill/submit_evaluationForm/<int:mentor_id>', views.submitEvaluationForm, name='submitEvaluationForm'),
    path('evaluate/', views.evaluation_view, name='evaluation_form'),
    path('evaluation/success/', views.evaluation_success, name='evaluation_success'),
    path('sendRequest/to/mentor/<int:mentor_id>', views.sendRequestToMentor, name='sendRequestToMentor'),
    
    
    
]
