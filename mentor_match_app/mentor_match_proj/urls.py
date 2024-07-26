from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from admin_mentor_app import views as user_views


urlpatterns = [
    path('', include("admin_mentor_app.urls")),
    path('admin/', admin.site.urls),
    path('login/', user_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('mentees/', include('mentees_app.urls')),
]
