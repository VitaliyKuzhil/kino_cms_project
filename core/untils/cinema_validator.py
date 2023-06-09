from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SeoValidator:  # Validator for Seo model
    @staticmethod
    def validate_keywords(value):  # Check cannot be None
        keywords = value.split(',')
        if not any(keywords):
            raise ValidationError(_('At least one keyword is required.'))


class MovieValidator:  # Validator for Movie model
    @staticmethod
    def validate_check_type(value):  # Check type Movie
        if not value:
            raise ValidationError(_('The type movie must be check.'))
