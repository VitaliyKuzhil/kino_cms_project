from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from cinema.models import Seo, Gallery
from datetime import datetime
from core.untils.universal_validator import PhotoValidatorMixin, UrlValidatorMixin, CounterValidatorMixin
from phonenumber_field.modelfields import PhoneNumberField
from core.untils.core_validator import TemplateValidator


class Pages(models.Model, PhotoValidatorMixin):  # Model Pages
    name_page = models.CharField(validators=[MinLengthValidator(1)], max_length=50, unique=True,
                                 help_text='Input name Page')
    gallery_page = models.OneToOneField(Gallery, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text='Select Gallery to Page')
    seo_page = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True,
                                    help_text='Select SEO to Page')
    status_page = models.BooleanField(default=True, help_text='Select status page')
    data_create_page = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name_page}'

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'
        ordering = ['data_create_page']


class HomePage(Pages):  # Model HomePage
    phone1 = PhoneNumberField(null=True, blank=True, unique=True, help_text='Input Phone number1')
    phone2 = PhoneNumberField(null=True, blank=True, unique=True, help_text='Input Phone number2')
    seo_text = models.TextField(null=True, blank=True, help_text='Input seo text')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_instance = HomePage.objects.first()
            if existing_instance:
                self.id = existing_instance.id
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_page = 'Home page'


class AboutCinemaPage(Pages):  # Model HomePage
    description = models.TextField(null=True, blank=True, help_text='Input description to Page')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_instance = AboutCinemaPage.objects.first()
            if existing_instance:
                self.id = existing_instance.id
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class NewsSharesPage(models.Model, PhotoValidatorMixin, UrlValidatorMixin):  # Model NewsSharesPage
    name = models.CharField(validators=[MinLengthValidator(1)], max_length=50,
                            help_text='Input name')
    description = models.TextField(null=True, blank=True, help_text='Input description to Page')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    url_address = models.URLField(null=True, blank=True, help_text='Input url address to Page')
    data_published = models.DateField(default=datetime.now)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True,
                               help_text='Select SEO')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)
        self.validate_url(self.url_address)

    class Meta:
        abstract = True


class NewsPage(NewsSharesPage):  # Model NewsPage
    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'
        ordering = ['name']


class SharesPage(NewsSharesPage):  # Model SharesPage
    class Meta:
        verbose_name = 'share'
        verbose_name_plural = 'shares'
        ordering = ['name']


class CafeBarPage(Pages):  # Model CafeBarPage
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    menu_cafe_bar = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                      help_text='Upload an image. Supported formats: JPEG, PNG')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_instance = CafeBarPage.objects.first()
            if existing_instance:
                self.id = existing_instance.id
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)
        self.validate_file_extension(self.menu_cafe_bar)
        self.validate_file_size(self.menu_cafe_bar)


class VipHallPage(Pages):  # Model VipHallPage
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_instance = VipHallPage.objects.first()
            if existing_instance:
                self.id = existing_instance.id
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class AdvertisePage(Pages):  # Model AdvertisePage
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_instance = AdvertisePage.objects.first()
            if existing_instance:
                self.id = existing_instance.id
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class ChildrenRoomPage(Pages):  # Model ChildrenRoomPage
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_instance = ChildrenRoomPage.objects.first()
            if existing_instance:
                self.id = existing_instance.id
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class ContactPage(models.Model, PhotoValidatorMixin):  # Model ContactPage
    logo_cinema = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                    help_text='Upload an image. Supported formats: JPEG, PNG')
    name_cinema = models.CharField(validators=[MinLengthValidator(1)], max_length=100, help_text='Input name Cinema')
    address_cinema = models.CharField(validators=[MinLengthValidator(1)], max_length=200, help_text='Input Address')
    location_cinema = models.DecimalField(max_digits=9, decimal_places=6, help_text='Input Location')

    def __init__(self, *args, **kwargs):
        if not Pages.objects.filter(name_page='Contacts page').exists():
            pages_instance = Pages(name_page='Contacts page')
            pages_instance.save()
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.logo_cinema)
        self.validate_file_size(self.logo_cinema)


class CustomPage(Pages):
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class Banners(models.Model, UrlValidatorMixin, CounterValidatorMixin):  # Abstract Model Banners
    name_banner = models.CharField(validators=[MinLengthValidator(1)], max_length=50, help_text='Input name Banner')
    status_banner = models.BooleanField(default=True, help_text='Select status Banner')

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class HomeBanner(Banners):  # Model HomeBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                          help_text='Select Gallery to Banner')
    url_banner = models.URLField(max_length=300, null=True, blank=True, help_text='Input url Banner')
    text_banner = models.TextField(null=True, blank=True, help_text='Input text to Banner')
    speed_banner = models.IntegerField(default=5, null=True, blank=True, help_text='Input speed to Banner')

    class Meta:
        verbose_name = 'home banner'
        verbose_name_plural = 'home banners'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_banner = self.__class__.__name__.lower()

    def clean(self):
        super().clean()
        self.validate_url(self.url_banner)
        self.count_integer(self.speed_banner)


class HomeNewsSharesBanner(Banners):  # Model HomeNewsSharesBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                          help_text='Select Gallery to Banner')
    url_banner = models.URLField(max_length=300, null=True, blank=True, help_text='Input url to Banner')
    speed_banner = models.IntegerField(default=5, null=True, blank=True, help_text='Input speed to Banner')

    class Meta:
        verbose_name = 'home news and shares banner'
        verbose_name_plural = 'home news and shares banners'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_banner = self.__class__.__name__.lower()

    def clean(self):
        super().clean()
        self.validate_url(self.url_banner)
        self.count_integer(self.speed_banner)


class BackgroundBanner(Banners):  # Model BackgroundBanner
    image_banner = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')

    class Meta:
        verbose_name = 'background banner'
        verbose_name_plural = 'background banners'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_banner = self.__class__.__name__.lower()


class ContextAdvertise(models.Model, PhotoValidatorMixin):  # Model ContextAdvertise
    photo_context = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                      help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.photo_context)
        self.validate_file_size(self.photo_context)

    class Meta:
        verbose_name = 'context advertise'
        verbose_name_plural = 'context advertises'


class MobileApplication(models.Model, UrlValidatorMixin):  # Model MobileApplication
    name_application = models.CharField(validators=[MinLengthValidator(1)], max_length=50,
                                        help_text='Input name to Application')
    description_application = models.TextField(null=True, blank=True, help_text='Input description to Application')
    gallery_application = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                               help_text='Select Gallery to Application')
    url_application = models.URLField(max_length=300, null=True, blank=True, help_text='Input url to Application')

    def clean(self):
        super().clean()
        self.validate_url(self.url_application)

    def __str__(self):
        return f'{self.name_application}'

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'
        ordering = ['name_application']


class SocialMedia(models.Model, UrlValidatorMixin):  # Model SocialMedia
    name_social = models.CharField(validators=[MinLengthValidator(1)], max_length=50, help_text='Input name to Social')
    url_social = models.URLField(max_length=300, null=True, blank=True, help_text='Input url to Social')

    def clean(self):
        super().clean()
        self.validate_url(self.url_social)

    def __str__(self):
        return f'{self.name_social}'

    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'socials'
        ordering = ['name_social']


class MailingTemplates(models.Model, TemplateValidator):  # Model MailingTemplates
    template_mailing = models.FileField(upload_to='static/mailing/', null=True, blank=True,
                                        help_text='Upload an file. Supported formats: HTML')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.template_mailing)

    def __str__(self):
        return f'{self.template_mailing.name}'

    class Meta:
        verbose_name = 'mailing template'
        verbose_name_plural = 'mailing templates'
