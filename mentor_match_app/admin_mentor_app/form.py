from django import forms

class EvaluationForm(forms.Form):
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
