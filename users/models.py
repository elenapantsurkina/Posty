from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name="Email")
    username = None
    password = models.CharField()
    date_birth = models.DateField(verbose_name="Дата рождения")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_editing = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
