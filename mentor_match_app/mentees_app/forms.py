
from django import forms
from .models import MenteeChallenge 
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column


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
    nationality = forms.CharField(max_length=50)

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
        
        # Set field attributes
        self.fields["password"].widget.attrs.update({"class": "form-control"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control", "readonly": "readonly"})
        self.fields["gender"].widget.attrs.update({"class": "form-control"})
        self.fields["telephone"].widget.attrs.update({"class": "form-control"})
        self.fields["nationality"].widget.attrs.update({"class": "form-control"})
        self.fields["dob"].widget.attrs.update({"class": "form-control", "type": "date"})

        # Layout with two fields per row
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gender', css_class='form-group col-md-6 mb-0'),
                Column('nationality', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dob', css_class='form-group col-md-6 mb-0'),
                Column('telephone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'role',
            'profile_picture',
        )