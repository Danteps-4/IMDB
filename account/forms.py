from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Firstname", min_length=4, max_length=40, widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Firstname", "id": "form-firstname"}))
    last_name = forms.CharField(label="Lastname", min_length=4, max_length=40, widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Lastname", "id": "form-lastname"}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Email", "id": "form-email"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["last_name"].required = False
        self.fields["first_name"].required = False

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["bio", "avatar"]
