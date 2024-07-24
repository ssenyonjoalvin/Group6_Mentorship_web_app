from .models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Goals, Evaluation

def global_data(request):
    users = User.objects.all()
    mentorship_matches = MentorshipMatch.objects.all()
    messages = Message.objects.all()
    notifications = Notification.objects.all()
    schedules = Schedule.objects.all()
    progress = Progress.objects.all()
    goals = Goals.objects.all()
    evaluations = Evaluation.objects.all()
    unread_notifications = Notification.objects.count()
    notifications = Notification.objects.all()

    
    
    return {
        'global_users': users,
        'global_mentorship_matches': mentorship_matches,
        'global_messages': messages,
        'global_notifications': notifications,
        'global_schedules': schedules,
        'global_progress': progress,
        'global_goals': goals,
        'global_evaluations': evaluations,
        'unread_notifications' : unread_notifications,
        'notifications':notifications
    }
