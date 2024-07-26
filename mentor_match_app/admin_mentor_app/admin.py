from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Evaluation

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('first_name', 'last_name', 'email', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'nationality', 'dob', 'telephone', 'profile_picture', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    # Ensure list_filter only includes fields from your User model
    list_filter = ('is_active', 'is_staff', 'role')  # Updated list_filter

admin.site.register(User, UserAdmin)


admin.site.register(MentorshipMatch)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Schedule)
admin.site.register(Progress)
admin.site.register(Evaluation)

