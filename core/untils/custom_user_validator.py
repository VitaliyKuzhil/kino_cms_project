from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserValidator:  # Validator for CustomUser model
    @staticmethod
    def birthday_validator(value):  # Check birthday day
        current_date = timezone.now().date()
        if value >= current_date:
            raise ValidationError(_('Invalid birthday day.'))
