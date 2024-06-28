from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterPageForm(forms.Form):
    username = forms.CharField(min_length=1 , max_length=20 , required=True , widget=forms.TextInput(attrs={"class":"form-control"}) , label="")

    def clean(self):
        cd = super().clean()
        username = cd.get('username')
        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            raise ValidationError("username already exists")