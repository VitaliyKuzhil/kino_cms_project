from django.db import models
from cinema.models import Seo, Gallery
from datetime import datetime


class Pages(models.Model):  # Model Pages
    id_page = models.AutoField(primary_key=True)
    name_page = models.CharField(max_length=50, null=False, blank=False)
    gallery_page = models.OneToOneField(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    seo_page = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True)
    status_page = models.BooleanField(default=True, null=False, blank=False)
    data_create_page = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'Page: {self.name_page}'

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ['data_create_page']


class HomePage(Pages):  # Model HomePage
    id_home_page = models.AutoField(primary_key=True)
    photo1 = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    photo2 = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)

    def __str__(self):
        return self.name_page


class NewsSharesPage(models.Model):  # Model NewsSharesPage
    id_news_shares = models.AutoField(primary_key=True)
    id_main_page = models.ForeignKey(Pages, on_delete=models.CASCADE, null=False, blank=False)
    type_page = models.CharField('TypePage', null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    url_address = models.URLField(max_length=300, null=True, blank=True)
    data_published = models.DateField(default=datetime.now)

    class Meta:
        abstract = True


class TypePage(models.Model):  # Model TypePage
    id_type_page = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class NewsPage(NewsSharesPage):  # Model NewsPage
    pass


class SharesPage(NewsSharesPage):  # Model SharesPage
    pass


class CafeBarPage(Pages):  # Model CafeBarPage
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    menu_cafe_bar = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)

    def __str__(self):
        return self.name_page


class VipHallPage(Pages):  # Model VipHallPage
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)

    def __str__(self):
        return self.name_page


class AdvertisePage(Pages):  # Model AdvertisePage
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)

    def __str__(self):
        return self.name_page


class ChildrenRoomPage(Pages):  # Model ChildrenRoomPage
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    main_photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)


class ContactPage(Pages):  # Model ContactPage
    id_cinema_contact = models.AutoField(primary_key=True)
    logo_cinema = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    name_cinema = models.CharField(max_length=100, null=False, blank=False)
    address_cinema = models.CharField(max_length=200, null=False, blank=False)
    location_cinema = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name_page


class Banners(models.Model):  # Abstract Model Banners
    id_banner = models.AutoField(primary_key=True)
    name_banner = models.CharField(max_length=50, null=False, blank=False)
    status_banner = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return f'Banner: {self.name_banner}'

    class Meta:
        abstract = True
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class HomeBanner(Banners):  # Model HomeBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    url_banner = models.URLField(max_length=300, null=True, blank=True)
    text_banner = models.TextField(null=True, blank=True)
    speed_banner = models.IntegerField(default=5, null=True, blank=True)


class HomeNewsSharesBanner(Banners):  # Model HomeNewsSharesBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    url_banner = models.URLField(max_length=300, null=True, blank=True)
    speed_banner = models.IntegerField(default=5, null=True, blank=True)


class BackgroundBanner(Banners):  # Model BackgroundBanner
    gallery_banner = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True)


class ContextAdvertise(models.Model):  # Model ContextAdvertise
    id_context = models.AutoField(primary_key=True)
    photo_context = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Context'
        verbose_name_plural = 'Contexts'


class MobileApplication(models.Model):  # Model MobileApplication
    id_application = models.AutoField(primary_key=True)
    name_application = models.CharField(max_length=50, null=False, blank=False)
    description_application = models.TextField(null=True, blank=True)
    gallery_application = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    url_application = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name_application

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['name_application']


class SocialMedia(models.Model):  # Model SocialMedia
    id_social = models.AutoField(primary_key=True)
    name_social = models.CharField(max_length=50, null=False, blank=False)
    url_social = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name_social

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['name_social']


class MailingTemplates(models.Model):  # Model MailingTemplates
    id_mailing = models.AutoField(primary_key=True)
    template_mailing = models.FileField(upload_to='static/mailing/%Y/%m/%d/', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'MailingTemplate'
        verbose_name_plural = 'MailingTemplates'
