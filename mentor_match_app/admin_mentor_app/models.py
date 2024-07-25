from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)  # Expanded to accommodate longer gender descriptions
    nationality = models.CharField(max_length=50)  # Expanded to accommodate longer country names
    dob = models.DateField()
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    
    role_choices = [
        ('1', 'Admin'),
        ('2', 'Mentor'),
        ('3', 'Mentee'),
    ]
    role = models.CharField(max_length=1, choices=role_choices)  # Use choices for role
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Add profile picture
    id = models.AutoField(primary_key=True)  # Auto increment primary key

    def __str__(self):
        return f"{self.full_name}"


class MentorshipMatch(models.Model):
    mentor = models.ForeignKey(User, related_name='mentor_matches', on_delete=models.CASCADE)
    mentee = models.ForeignKey(User, related_name='mentee_matches', on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)
    
    status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    file = models.FileField(upload_to='message_files/', blank=True, null=True)  # Add FileField for attachments
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.full_name} to {self.receiver.full_name} ({self.sent_at})"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Schedule(models.Model):
    mentor = models.ForeignKey(User, related_name='mentor_schedules', on_delete=models.CASCADE)
    mentee = models.ForeignKey(User, related_name='mentee_schedules', on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    
    status_choices = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='scheduled')


class Progress(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    goal = models.CharField(max_length=255)
    milestone = models.CharField(max_length=255, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    progress_date = models.DateTimeField(auto_now_add=True)


class Evaluation(models.Model):
    mentorship_match = models.ForeignKey(MentorshipMatch, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, related_name='mentor_evaluations', on_delete=models.CASCADE)
    mentee = models.ForeignKey(User, related_name='mentee_evaluations', on_delete=models.CASCADE)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    technical_skills = models.PositiveSmallIntegerField()
    communication_skills = models.PositiveSmallIntegerField()
    problem_solving_skills = models.PositiveSmallIntegerField()
    time_management = models.PositiveSmallIntegerField()
    team_collaboration = models.PositiveSmallIntegerField()
    comments = models.TextField(blank=True, null=True)
