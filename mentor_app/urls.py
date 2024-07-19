from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='registration'),
    path('mentees/', views.get_mentees, name='mentees'),
    path('preview_mentee/', views.preview_mentee, name='mentee_preview'),
    path('choice_user_type/', views.choice_user_type, name='choice_user_type'),
    path('registration_success/', TemplateView.as_view(template_name='registration_success.html'), name='registration_success'),
    path('mentor_registration/',views.mentor_registration, name='mentor_registration'),
]