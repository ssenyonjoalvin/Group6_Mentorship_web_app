from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Evaluation

class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'gender', 'nationality', 'dob', 'telephone', 'status', 'role')
    search_fields = ('full_name', 'email', 'telephone')
    list_filter = ('gender', 'nationality', 'status', 'role')

class MentorshipMatchAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'match_date', 'status')
    search_fields = ('mentor__full_name', 'mentee__full_name')
    list_filter = ('status', 'match_date')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'sent_at')
    search_fields = ('sender__full_name', 'receiver__full_name', 'content')
    list_filter = ('sent_at',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    search_fields = ('user__full_name', 'message')
    list_filter = ('is_read', 'created_at')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'session_date', 'status')
    search_fields = ('mentor__full_name', 'mentee__full_name')
    list_filter = ('status', 'session_date')

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'goal', 'milestone', 'progress_date')
    search_fields = ('goal', 'milestone')
    list_filter = ('progress_date',)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('mentorship_match', 'mentor', 'mentee', 'evaluation_date', 'technical_skills', 'communication_skills', 'problem_solving_skills', 'time_management', 'team_collaboration')
    search_fields = ('mentor__full_name', 'mentee__full_name', 'comments')
    list_filter = ('evaluation_date',)

admin.site.register(User, UserAdmin)
admin.site.register(MentorshipMatch, MentorshipMatchAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
