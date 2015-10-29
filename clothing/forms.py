from django import forms
# from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm







class CustomLoginForm(AuthenticationForm):

    error_messages = {
        'invalid_credentials': 'fffffffffffffffffffffffNote that both fields may be case-sensitive.'
    }
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data['password'] # self.cleaned_data.get same as self.cleaned_data.

        print
        print
        print username
        print password
        print
        print
        return 

        # if username and password:
        #     user = authenticate(request, username=username, password=password)
        #     login(request, user)
        #     return HttpResponseRedirect('/dashboard/')
            # raise forms.ValidationError(
            #     self.error_messages['invalid_credentials'],
            #     code='invalid_credentials'
            # )
            # return http
            # user = authenticate(username=username, password=password)
            # print
            # print user
            # print 
            # print
        # else:
        #     raise forms.ValidationError(
        #         self.error_messages['invalid_credentials'],
        #         code='invalid_credentials'
        #     )
        # return self.cleaned_data




class GatewayForm(AuthenticationForm):
    username = forms.EmailField(label=_("My email address is"))
    GUEST, NEW, EXISTING = 'anonymous', 'new', 'existing'
    CHOICES = (
        (GUEST, _('I am a new customer and want to checkout as a guest')),
        (NEW, _('I am a new customer and want to create an account '
                'before checking out')),
        (EXISTING, _('I am a returning customer, and my password is')))
    options = forms.ChoiceField(widget=forms.widgets.RadioSelect,
                                choices=CHOICES, initial=GUEST)

    def clean_username(self):
        return normalise_email(self.cleaned_data['username'])

    def clean(self):
        if self.is_guest_checkout() or self.is_new_account_checkout():
            if 'password' in self.errors:
                del self.errors['password']
            if 'username' in self.cleaned_data:
                email = normalise_email(self.cleaned_data['username'])
                if User._default_manager.filter(email__iexact=email).exists():
                    msg = "A user with that email address already exists"
                    self._errors["username"] = self.error_class([msg])
            return self.cleaned_data
        return super(GatewayForm, self).clean()

    def is_guest_checkout(self):
        return self.cleaned_data.get('options', None) == self.GUEST

    def is_new_account_checkout(self):
        return self.cleaned_data.get('options', None) == self.NEW






SIZES_CHOICES = (
    ('x-small', 'X-Small'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('x-large', 'X-Large'),
)

class SizeForm(forms.Form):
    sizes = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=SIZES_CHOICES)