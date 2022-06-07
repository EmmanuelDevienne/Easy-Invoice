from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView

from accounts.forms import UserRegistrationForm, UserloginForm, ResetPasswordForm, SetNewPassword, \
    ProfilForm, ChangePasswordForm, UserImageForm
from accounts.models import CustomUser


class Signup(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:login')


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserloginForm

    def get_success_url(self):
        return reverse_lazy('accounts:profile')


class Logout(LogoutView):
    def get_next_page(self):
        return reverse_lazy('accounts:login')


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/password_change_form.html"
    form_class = ChangePasswordForm
    success_url = reverse_lazy('accounts:password_change_done')


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class PasswordReset(PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    form_class = ResetPasswordForm

    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_subject.txt"
    success_url = reverse_lazy("accounts:password_reset_done")


class PasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy("accounts:password_reset_complete")
    template_name = "accounts/password_reset_confirm.html"
    form_class = SetNewPassword


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


class UpdateProfil(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfilForm
    form2_class = UserImageForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateProfil, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        elif 'form2' not in context:
            context['form2'] = self.form2_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        change_name_form = ProfilForm(data=request.POST, instance=request.user)
        user_image_form = UserImageForm(request.POST, request.FILES, instance=request.user)
        action = self.request.POST['action']

        if action == 'change_information':
            if change_name_form.is_valid():
                change_name_form.save()
                return super().post(request, *args, **kwargs)
            else:
                return super().post(request, *args, **kwargs)

        elif action == 'change_image':
            if user_image_form.is_valid():
                user_image_form.save()
                return redirect("accounts:profile")
            else:
                return super().post(request, *args, **kwargs)

        else:
            return super().post(request, *args, **kwargs)
