"""from django.core.validators import MinLengthValidator
from django.db import models
from cinema.models import Seo, Gallery
from datetime import datetime
from core.constants import TypePageChoices
from core.untils.universal_validator import PhotoValidatorMixin, UrlValidatorMixin, CounterValidatorMixin


class Pages(models.Model, PhotoValidatorMixin):  # Model Pages
    name_page = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False,
                                 help_text='Input name Page')
    gallery_page = models.OneToOneField(Gallery, on_delete=models.CASCADE, null=True, blank=True,
                                        help_text='Select Gallery to Page')
    seo_page = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True,
                                    help_text='Select SEO to Page')
    status_page = models.BooleanField(default=True, null=False, blank=False, help_text='Select status page')
    data_create_page = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'{self.name_page}'

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'
        ordering = ['data_create_page']


class HomePage(Pages):  # Model HomePage
    photo1 = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                               help_text='Upload an image. Supported formats: JPEG, PNG')
    photo2 = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                               help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.photo1)
        self.validate_file_size(self.photo1)
        self.validate_file_extension(self.photo2)
        self.validate_file_size(self.photo2)


class NewsSharesPage(models.Model, PhotoValidatorMixin, UrlValidatorMixin):  # Model NewsSharesPage
    id_main_page = models.ForeignKey(Pages, on_delete=models.CASCADE, null=False, blank=False,
                                     help_text='Select Page')
    type_page = models.CharField(choices=TypePageChoices, default=TypePageChoices.NEWS, null=False, blank=False, help_text='Select type Page')
    description = models.TextField(null=True, blank=True, help_text='Include description to Page')
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    url_address = models.URLField(null=True, blank=True, help_text='Input url address to Page')
    data_published = models.DateField(default=datetime.now)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)
        self.validate_url(self.url_address)

    class Meta:
        abstract = True


class NewsPage(NewsSharesPage):  # Model NewsPage
    pass


class SharesPage(NewsSharesPage):  # Model SharesPage
    pass


class CafeBarPage(Pages):  # Model CafeBarPage
    title = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input title')
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')
    menu_cafe_bar = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                      help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)
        self.validate_file_extension(self.menu_cafe_bar)
        self.validate_file_size(self.menu_cafe_bar)


class VipHallPage(Pages):  # Model VipHallPage
    title = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input title')
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class AdvertisePage(Pages):  # Model AdvertisePage
    title = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input title')
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class ChildrenRoomPage(Pages):  # Model ChildrenRoomPage
    title = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input title')
    description = models.TextField(null=True, blank=True, help_text='Input description')
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                   help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_photo)
        self.validate_file_size(self.main_photo)


class ContactPage(Pages):  # Model ContactPage
    logo_cinema = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                    help_text='Upload an image. Supported formats: JPEG, PNG')
    name_cinema = models.CharField(validators=[MinLengthValidator(10)], max_length=100, null=False, blank=False, help_text='Input name Cinema')
    address_cinema = models.CharField(validators=[MinLengthValidator(10)], max_length=200, null=False, blank=False, help_text='Input Address')
    location_cinema = models.DecimalField(max_digits=9, decimal_places=6, help_text='Input Location')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.logo_cinema)
        self.validate_file_size(self.logo_cinema)


class Banners(models.Model, UrlValidatorMixin, CounterValidatorMixin):  # Abstract Model Banners
    name_banner = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input name Banner')
    status_banner = models.BooleanField(default=True, null=False, blank=False, help_text='Select status Banner')

    def __str__(self):
        return f'{self.name_banner}'

    class Meta:
        abstract = True
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class HomeBanner(Banners):  # Model HomeBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                          help_text='Select Gallery to Banner')
    url_banner = models.URLField(max_length=300, null=True, blank=True, help_text='Input url Banner')
    text_banner = models.TextField(null=True, blank=True, help_text='Input text to Banner')
    speed_banner = models.IntegerField(default=5, null=True, blank=True, help_text='Input speed to Banner')

    def clean(self):
        super().clean()
        self.validate_url(self.url_banner)
        self.count_integer(self.speed_banner)


class HomeNewsSharesBanner(Banners):  # Model HomeNewsSharesBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                          help_text='Select Gallery to Banner')
    url_banner = models.URLField(max_length=300, null=True, blank=True, help_text='Input url to Banner')
    speed_banner = models.IntegerField(default=5, null=True, blank=True, help_text='Input speed to Banner')

    def clean(self):
        super().clean()
        self.validate_url(self.url_banner)
        self.count_integer(self.speed_banner)


class BackgroundBanner(Banners):  # Model BackgroundBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                          help_text='Select Gallery to Banner')


class ContextAdvertise(models.Model, PhotoValidatorMixin):  # Model ContextAdvertise
    photo_context = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True,
                                      help_text='Upload an image. Supported formats: JPEG, PNG')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.photo_context)
        self.validate_file_size(self.photo_context)


class MobileApplication(models.Model, UrlValidatorMixin):  # Model MobileApplication
    name_application = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input name to Application')
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
    name_social = models.CharField(validators=[MinLengthValidator(10)], max_length=50, null=False, blank=False, help_text='Input name to Social')
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


class MailingTemplates(models.Model, PhotoValidatorMixin):  # Model MailingTemplates
    template_mailing = models.FileField(upload_to='static/mailing/%Y/%m/%d/', editable=False, null=True, blank=True,
                                        help_text='Upload an file. Supported formats: HTML')

    def clean(self):
        super().clean()
        self.validate_file_extension(self.template_mailing)
        self.validate_file_size(self.template_mailing)

    def __str__(self):
        return f'{self.template_mailing.name}'

    class Meta:
        verbose_name = 'mailing template'
        verbose_name_plural = 'mailing templates'
"""