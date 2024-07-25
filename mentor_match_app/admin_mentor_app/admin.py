from django.contrib import admin
from .models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Evaluation

# Register your models here
admin.site.register(User)
admin.site.register(MentorshipMatch)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Schedule)
admin.site.register(Progress)
admin.site.register(Evaluation)
