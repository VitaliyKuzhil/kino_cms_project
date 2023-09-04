from django.db import models


class TypePageChoices(models.TextChoices):
    NEWS = ('news', 'News')
    SHARES = ('shares', 'Shares')


STATUS_CHOICES = (
    (True, 'On'),
    (False, 'Off'),
)
