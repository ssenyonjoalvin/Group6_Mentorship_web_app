
from django import forms
from .models import MenteeChallenge 
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]

class MenteeChallengeForm(forms.ModelForm):
    class Meta:
        model = MenteeChallenge
        fields = ['challenge_1', 'challenge_2', 'challenge_3', 'challenge_4', 'challenge_5', 'description']

class MenteeProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    telephone = forms.CharField(max_length=50)
    email = forms.EmailField()
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    telephone = forms.CharField(max_length=50)
    nationality = forms.CharField(max_length=50)
    # type_of_user = forms.ChoiceField(choices=TYPE_OF_USER)
    
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "gender",
            "nationality",
            "dob",
            "telephone",
            "role",
            "profile_picture",
          
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Register"))
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["gender"].widget.attrs.update({"class": "form-control"})
        self.fields["telephone"].widget.attrs.update({"class": "form-control"})
        self.fields["nationality"].widget.attrs.update({"class": "form-control"})
        # self.fields["type_of_user"].widget.attrs.update({"class": "form-control"})
        self.fields["dob"] = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"})
)
        