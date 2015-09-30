from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        user_profile = UserProfile(user=user)
        if commit:
            user.save()
            user_profile.save()
        return user, user_profile





SIZES_CHOICES = (
    ('x-small', 'X-Small'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('x-large', 'X-Large'),
)

class SizeForm(forms.Form):
    sizes = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=SIZES_CHOICES)