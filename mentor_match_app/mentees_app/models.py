from django.db import models
from admin_mentor_app.models import User

class MenteeChallenge(models.Model):
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenges')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentees')
    challenge_1 = models.CharField(max_length=255)
    challenge_2 = models.CharField(max_length=255, blank=True, null=True)
    challenge_3 = models.CharField(max_length=255, blank=True, null=True)
    challenge_4 = models.CharField(max_length=255, blank=True, null=True)
    challenge_5 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"Challenges for {self.mentee} mentored by {self.mentor}"
    
