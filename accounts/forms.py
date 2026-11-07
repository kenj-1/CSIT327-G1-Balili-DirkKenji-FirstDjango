from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            "course": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. BSCS, BSIT'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "course")
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            "course": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. BSCS, BSIT'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
