from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Enter E-mail...',
        })

class CustomSetPasswordForm(SetPasswordForm):

     def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = """<p class="text-start mb-0">Your password can't be too similar to your other personal information.</br>
        Your password can't be the same as your old password.</br>
        Your password must contain at least 8 characters.</br>
        Your password can't be a commonly used password.</br>
        Your password can't be entirely numeric.</p>"""
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'new_password1',
            'type': 'password',
            'placeholder': 'Enter password...'
        })
        self.fields['new_password2'].help_text = """<p class="text-start mb-0">Enter the same password as before, for verification.</p>"""
        self.fields['new_password2'].label = 'Confirm password'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'new_password2',
            'type': 'password',
            'placeholder': 'Confirm password...'
        })