# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.hashers import make_password
from .models import Schedule


# GENDER_CHOICES = [
#     ('M', 'Male'),
#     ('F', 'Female'),
#     ('O', 'Other'),
# ]

# TYPE_OF_USER = [
#     ('1', 'Mentor'),
#     ('2', 'Mentee'),

# ]

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)
#     telephone = forms.CharField(max_length=50)
#     nationality = forms.CharField(max_length=50)
#     type_of_user = forms.CharField(max_length=50)  # Adjust as needed

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'gender', 'telephone', 'nationality', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Register'))
#         self.fields['username'].widget.attrs.update({'class': 'form-control'})
#         self.fields['email'].widget.attrs.update({'class': 'form-control'})
#         self.fields['gender'].widget.attrs.update({'class': 'form-control'})
#         self.fields['telephone'].widget.attrs.update({'class': 'form-control'})
#         self.fields['nationality'].widget.attrs.update({'class': 'form-control'})

# forms.py
from django import forms
from django.contrib.auth import get_user_model

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]
AVAILABILITY_CHOICES = [
    ('Available',"Present"),
    ('Not Available', "Absent"),
]
EXPERTISE_CHOICES = [
    ("Software Development",'Software Development'),
    ("Data Science and Analytics",'Data Science and Analytics'),
    ('Cybersecurity',"Cybersecurity"),
    ('Cloud Computing',"Cloud Computing"),
    ('Networking and Telecommunications',"Networking and Telecommunications"),
    ('Blockchain and Cryptocurrency',"Blockchain and Cryptocurrency"),
    ('Virtual Reality (VR) and Augmented Reality (AR)',"Virtual Reality (VR) and Augmented Reality (AR)"),
    ('Digital Marketing',"Digital Marketing"),
]



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
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
class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    telephone = forms.CharField(max_length=50)
    email = forms.EmailField()
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    telephone = forms.CharField(max_length=50)
    nationality = forms.CharField(max_length=50)
    expertise = forms.ChoiceField(choices=EXPERTISE_CHOICES)
    availability = forms.ChoiceField(choices=AVAILABILITY_CHOICES)
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
            "expertise",
            "availability",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Register"))
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["gender"].widget.attrs.update({"class": "form-control"})
        self.fields["expertise"].widget.attrs.update({"class": "form-control"})
        self.fields["availability"].widget.attrs.update({"class": "form-control"})
        self.fields["telephone"].widget.attrs.update({"class": "form-control"})
        self.fields["nationality"].widget.attrs.update({"class": "form-control"})
        # self.fields["type_of_user"].widget.attrs.update({"class": "form-control"})
        self.fields["dob"] = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"})
)
        

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['mentee', 'session_date', 'status']
        widgets = {
            'session_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.HiddenInput(),  # We'll set this to 'scheduled' in the view
        }


class EditAppointmentForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['session_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['session_date'].widget = forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        )

    def clean_session_date(self):
        date_time = self.cleaned_data.get('session_date')
        if date_time:
            return date_time
        raise forms.ValidationError("This field is required.")        