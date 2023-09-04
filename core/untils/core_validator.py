from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class TemplateValidator:  # Universal Photo Validator
    @staticmethod
    def validate_file_extension(value):  # Valid extension Image
        allowed_extensions = ('.html',)
        if value:
            file_extension = value.name.rstrip('.')
            if not file_extension.endswith(allowed_extensions):
                raise ValidationError(_('Unsupported file format. Please upload a html file.'))
