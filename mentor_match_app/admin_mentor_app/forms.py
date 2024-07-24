# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.hashers import make_password


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

# TYPE_OF_USER = [
#     ("1", "Mentor"),
#     ("2", "Mentee"),
# ]


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
<<<<<<< HEAD
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_of_user'].widget.attrs.update({'class': 'form-control'})
       
       
class EvaluationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    support = forms.MultipleChoiceField(
        choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Bad', 'Bad'), ('Very Bad', 'Very Bad')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    communication = forms.MultipleChoiceField(
        choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Bad', 'Bad'), ('Very Bad', 'Very Bad')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    confidence = forms.MultipleChoiceField(
        choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Bad', 'Bad'), ('Very Bad', 'Very Bad')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    career = forms.MultipleChoiceField(
        choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Bad', 'Bad'), ('Very Bad', 'Very Bad')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    understanding = forms.MultipleChoiceField(
        choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Bad', 'Bad'), ('Very Bad', 'Very Bad')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    comfort = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    goals = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    recommend = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    resources = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    additional_resources = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    additional_comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
=======
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Register"))
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["gender"].widget.attrs.update({"class": "form-control"})
        self.fields["telephone"].widget.attrs.update({"class": "form-control"})
        self.fields["nationality"].widget.attrs.update({"class": "form-control"})
        # self.fields["type_of_user"].widget.attrs.update({"class": "form-control"})
        self.fields["dob"] = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"})
)
>>>>>>> main
