from django.urls import path

from accounts.views import Signup, Login, Logout, PasswordChange, PasswordChangeDone, \
    PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete, \
    UpdateProfil

app_name = "accounts"

urlpatterns = [
    path('register/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", Logout.as_view(), name="logout"),

    path("password_reset/", PasswordReset.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDone.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetComplete.as_view(), name="password_reset_complete"),

    path('profile/', UpdateProfil.as_view(), name="profile"),

    path("password_change/", PasswordChange.as_view(), name="password_change"),
    path("password_change/done/", PasswordChangeDone.as_view(), name="password_change_done"),

]
