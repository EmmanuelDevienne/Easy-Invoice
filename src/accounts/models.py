import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("You must enter an email.")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name)

        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


def get_image_path(instance, filename):
    return os.path.join('users', str(instance.id), filename)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    email = models.EmailField(max_length=50, blank=False, unique=True)
    first_name = models.CharField(max_length=50, blank=False, verbose_name="First name")
    last_name = models.CharField(max_length=50, blank=False, verbose_name="Last Name")

    profile_image = models.ImageField(default='/users/default.png', upload_to=get_image_path, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    ordering = ('email',)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @staticmethod
    def get_absolute_url():  # Redirection after register
        return reverse('home')

    class Meta:
        ordering = ['last_name']
        verbose_name = "User"

    def __str__(self):
        return self.first_name

