from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager  # class override
from django.utils import timezone  # Data.now
from .constants import GenderChoices, LANGUAGE_CHOICES, CITY_CHOICES  # Choices
from phonenumber_field.modelfields import PhoneNumberField  # PhoneNumber
from creditcards.models import CardNumberField  # CardNumber
from core.untils.custom_user_validator import UserValidator  # Validator


class CustomUserManager(UserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# Custom User Model (for extend the base model)
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, help_text='Input email')
    gender = models.CharField(choices=GenderChoices.choices, default=GenderChoices.MALE, null=True, blank=True,
                              help_text='Select Gender')
    birthday = models.DateField(default=timezone.now, null=True, blank=True,
                                validators=[UserValidator.birthday_validator], help_text='Select day birthday')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='English', null=True, blank=True,
                                help_text='Select Language')
    phone = PhoneNumberField(null=True, blank=True, unique=True, help_text='Input Phone number')
    city = models.CharField(choices=CITY_CHOICES, default='washington', null=True, blank=True, help_text='Select City')
    number_card = CardNumberField(null=True, blank=True, unique=True, help_text='Input Card number')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['date_joined']

