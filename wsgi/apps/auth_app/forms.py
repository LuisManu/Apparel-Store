from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile

class CustomUsernameField(forms.CharField):
    '''
    Used to turn/save username lowercase even when user uses caps with text-transform:lowercase on.
    '''
    def to_python(self, value):
        return value.lower()



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = CustomUsernameField(required=True, widget=forms.TextInput(attrs={'style': 'text-transform:lowercase;'}))

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})

    def clean_email(self):
        error_messages = {
            'duplicate_email': 'A user with this email address already exists'
        }

        email = self.cleaned_data["email"]
       
        try:
            User._default_manager.get(email=email)
            raise forms.ValidationError(error_messages['duplicate_email'], code='duplicate_email')
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        user_profile = UserProfile(user=user)

        if commit:
            user.save()
            user_profile.save()
        return user, user_profile

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")