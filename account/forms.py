from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Account


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'first_name',
            'type': 'text',
            'placeholder': 'Enter first name...'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'last_name',
            'type': 'text',
            'placeholder': 'Enter last name...'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Enter username...'
        })
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Enter E-mail...',
        })
        self.fields['password1'].help_text = """<p class="text-start mb-0">Your password can't be too similar to your other personal information.</br>
        Your password must contain at least 8 characters.</br>
        Your password can't be a commonly used password.</br>
        Your password can't be entirely numeric.</p>"""
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'Enter password...'
        })
        self.fields['password2'].label = 'Confirm password'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'Confirm password...'
        })


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Full Name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
            'type': 'text',
            'placeholder': 'Enter Your full name...'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Enter username...'
        })
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Enter E-mail...',
        })


class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].help_text = """<p class="text-start mb-0">Enter your old password.</p>"""
        self.fields['old_password'].label = 'Old password'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'old_password',
            'type': 'password',
            'placeholder': 'Enter old password...'
        })
        self.fields['new_password1'].help_text = """<p class="text-start mb-0">Your password can't be too similar to your other personal information.</br>
        Your password can't be the same as your old password.</br>
        Your password must contain at least 8 characters.</br>
        Your password can't be a commonly used password.</br>
        Your password can't be entirely numeric.</p>"""
        self.fields['new_password1'].label = 'New password'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'new_password1',
            'type': 'password',
            'placeholder': 'Enter new password...'
        })
        self.fields['new_password2'].help_text = """<p class="text-start mb-0">Enter the same password as before, for verification.</p>"""
        self.fields['new_password2'].label = 'New password confirmation'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'new_password2',
            'type': 'password',
            'placeholder': 'Confirm new password...'
        })
