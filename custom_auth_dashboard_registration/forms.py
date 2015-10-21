from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from utils import normalise_email, existing_user_fields


class UserForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        kwargs['instance'] = user
        super(UserForm, self).__init__(*args, **kwargs)
        if 'email' in self.fields:
            self.fields['email'].required = True

    def clean_email(self):
        """
        Make sure that the email address is aways unique as it is
        used instead of the username. This is necessary because the
        unique-ness of email addresses is *not* enforced on the model
        level in ``django.contrib.auth.models.User``.
        """
        email = self.cleaned_data['email']
        if User._default_manager.filter(
                email__iexact=email).exclude(id=self.user.id).exists():
            raise ValidationError(
                _("A user with this email address already exists"))
        # Save the email unaltered
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']




























































# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import UserProfile



# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=True)
#         user.email = self.cleaned_data["email"]
#         user_profile = UserProfile(user=user)
#         if commit:
#             user.save()
#             user_profile.save()
#         return user, user_profile