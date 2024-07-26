
from django import forms
from .models import MenteeChallenge

class MenteeChallengeForm(forms.ModelForm):
    class Meta:
        model = MenteeChallenge
        fields = ['challenge_1', 'challenge_2', 'challenge_3', 'challenge_4', 'challenge_5', 'description']
