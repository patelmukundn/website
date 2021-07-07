from django import forms
from django.forms.widgets import Textarea


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your Name must not be empty!",
        "max_length": "Please enter shorter name under 100 char!"
    })
    review_text = forms.CharField(
        label="Your Feedback", max_length=200, widget=Textarea)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
