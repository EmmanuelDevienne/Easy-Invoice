from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, \
    PasswordChangeForm

from accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.helper.add_input(Submit('submit', 'Sign in', css_class=""))

        self.helper.layout = Layout(
            AppendedText('email', '<span class="fas fa-envelope"></span>', placeholder="Email", autofocus=""),
            AppendedText('first_name', '<span class="fas fa-user"></span>', placeholder="First Name"),
            AppendedText('last_name', '<span class="fas fa-user"></span>', placeholder="Last Name"),
            AppendedText('password1', '<i class="fas fa-lock"></i>', placeholder="Password"),
            AppendedText('password2', '<i class="fas fa-lock"></i>', placeholder="Password Verification"),
        )

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")


class UserImageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Apply', css_class="col-6 mycenter"))

    class Meta:
        model = CustomUser
        fields = ('profile_image',)


class UserloginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Sign in', css_class=""))

        self.helper.layout = Layout(
            AppendedText('username', '<span class="fas fa-envelope"></span>', placeholder="Email", autofocus=""),
            AppendedText('password', '<i class="fas fa-lock"></i>', placeholder="Password"),
        )

    class Meta:
        model = CustomUser
        fields = "email"


class ResetPasswordForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Request new password', css_class="btn-block"))

        self.helper.layout = Layout(
            AppendedText('email', '<span class="fas fa-envelope"></span>', placeholder="Email", autofocus=""),
        )

    class Meta:
        model = CustomUser
        fields = "email"


class SetNewPassword(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        self.helper.add_input(Submit('submit', 'Set New Password', css_class="btn-block"))

        self.helper.layout = Layout(
            AppendedText('new_password1', '<i class="fas fa-lock"></i>', placeholder="Password"),
            AppendedText('new_password2', '<i class="fas fa-lock"></i>', placeholder="Password verification"),
        )

    class Meta:
        model = CustomUser
        fields = ("password1", "password2")


class ProfilForm(forms.ModelForm):
    prefix = 'change_information'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = True

        self.helper.add_input(Submit('submit', 'Update', css_class="", css_id=""))

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            AppendedText('email', '<span class="fas fa-envelope"></span>'),
            AppendedText('first_name', '<span class="fas fa-user"></span>'),
            AppendedText('last_name', '<span class="fas fa-user"></span>'),

        )

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")


class ChangePasswordForm(PasswordChangeForm):
    prefix = 'change_password'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        self.helper.add_input(Submit('change_password', 'Change Password', css_class=""))

        self.helper.layout = Layout(
            AppendedText('old_password', '<i class="fas fa-lock"></i>', placeholder="Old Password"),
            AppendedText('new_password1', '<i class="fas fa-lock"></i>', placeholder="New Password"),
            AppendedText('new_password2', '<i class="fas fa-lock"></i>', placeholder="New Password Confirmation"),
        )

    class Meta:
        model = PasswordChangeForm
        fields = ("old_password", "new_password1", "new_password2")
