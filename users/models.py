from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    date_birth = models.DateField(verbose_name='Дата рождения', null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_editing = models.DateTimeField(auto_now=True, blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Последний вход')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # def clean(self):
    #     super().clean()
    #
    #     "Валидация уникальности email"
    #     if self.email and User.objects.exclude(pk=self.pk).filter(email=self.email).exists():
    #         raise ValidationError("Этот адрес электронной почты уже используется.")
    #
    #     "Валидация email-домена"
    #     valid_domains = ['mail.ru', 'yandex.ru']
    #     domain = self.email.split("@")[-1]
    #     if domain not in valid_domains:
    #         raise ValidationError("Домен электронной почты должен быть mail.ru или yandex.ru.")
    #
    #     "Валидация пароля"
    #     if not self.password_valid(self.raw_password):
    #         raise ValidationError("Пароль должен содержать не менее 8 символов и включать цифры.")
    #
    # def password_valid(self, password):
    #     return len(password) >= 8 and re.search(r'\d', password)
    #
    # def __str__(self):
    #     return self.email
    #
    # def set_password(self, raw_password):
    #     self.raw_password = raw_password  # Сохраняем нешифрованный пароль для валидации
    #     super().set_password(raw_password)
