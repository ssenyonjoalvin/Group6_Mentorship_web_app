from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include("admin_mentor_app.urls")),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='admin_mentor_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='admin_mentor_app/login.html'), name='logout'),
    path('mentees/', include('mentees_app.urls')),
]
