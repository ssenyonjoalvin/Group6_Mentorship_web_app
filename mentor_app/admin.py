from django.contrib import admin
from .models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Evaluation

# Register your models here.
# admin.py
from django.contrib import admin
from .models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Evaluation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role')
    search_fields = ('full_name', 'email')
    list_filter = ('role', 'gender', 'nationality')

@admin.register(MentorshipMatch)
class MentorshipMatchAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'match_date', 'status')
    list_filter = ('status',)
    search_fields = ('mentor__full_name', 'mentee__full_name')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'sent_at')
    search_fields = ('sender__full_name', 'receiver__full_name')
    list_filter = ('sent_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    search_fields = ('user__full_name', 'message')
    list_filter = ('is_read', 'created_at')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'session_date', 'status')
    search_fields = ('mentor__full_name', 'mentee__full_name')
    list_filter = ('status', 'session_date')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'goal', 'milestone', 'progress_date')
    search_fields = ('goal', 'milestone')
    list_filter = ('progress_date',)

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('mentorship_match', 'mentor', 'mentee', 'evaluation_date', 'technical_skills', 'communication_skills', 'problem_solving_skills', 'time_management', 'team_collaboration')
    search_fields = ('mentor__full_name', 'mentee__full_name', 'comments')
    list_filter = ('evaluation_date',)

