from django.contrib import admin
from .models import Pages, HomePage, AboutCinemaPage, NewsPage, SharesPage, CafeBarPage, VipHallPage, AdvertisePage,\
    ChildrenRoomPage, ContactPage, CustomPage, Banners, HomeBanner, HomeNewsSharesBanner, BackgroundBanner,\
    ContextAdvertise, MobileApplication, SocialMedia, MailingTemplates


class PagesAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'gallery_page', 'seo_page', 'status_page', 'data_create_page']
    search_fields = ['name_page']
    list_filter = ['status_page', 'data_create_page']
    ordering = ['data_create_page']
    # list_editable = []
    fields = ['name_page', 'gallery_page', 'seo_page', 'status_page']
    # readonly_fields = ['create_time', 'update_time']


class HomePageAdmin(admin.ModelAdmin):
    list_display = ['phone1', 'phone2', 'seo_text', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['phone1', 'phone2', 'seo_text', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class AboutCinemaPageAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class NewsPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'main_photo', 'url_address', 'data_published', 'seo']
    search_fields = ['name']
    list_filter = ['data_published']
    # list_editable = []
    fields = ['name', 'description', 'main_photo', 'url_address', 'seo']
    # readonly_fields = ['create_time', 'update_time']


class SharesPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'main_photo', 'url_address', 'data_published', 'seo']
    search_fields = ['name']
    list_filter = ['data_published']
    # list_editable = []
    fields = ['name', 'description', 'main_photo', 'url_address', 'seo']
    # readonly_fields = ['create_time', 'update_time']


class CafeBarPageAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'description', 'main_photo', 'menu_cafe_bar', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_page', 'description', 'main_photo', 'menu_cafe_bar', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class VipHallPageAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class AdvertisePageAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class ChildrenRoomPageAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class CustomPageAdmin(admin.ModelAdmin):
    list_display = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_page', 'description', 'main_photo', 'gallery_page', 'seo_page']
    # readonly_fields = ['create_time', 'update_time']


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ['name_cinema', 'logo_cinema', 'address_cinema', 'location_cinema']
    search_fields = ['title']
    list_filter = []
    # list_editable = []
    fields = ['name_cinema', 'logo_cinema', 'address_cinema', 'location_cinema']
    # readonly_fields = ['create_time', 'update_time']


class BannersAdmin(admin.ModelAdmin):
    list_display = ['name_banner', 'status_banner']
    search_fields = ['name_banner']
    list_filter = []
    # list_editable = []
    fields = ['name_banner', 'status_banner']
    # readonly_fields = ['create_time', 'update_time']


class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ['gallery_banner', 'url_banner', 'text_banner', 'speed_banner']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['gallery_banner', 'url_banner', 'text_banner', 'speed_banner']
    # readonly_fields = ['create_time', 'update_time']


class HomeNewsSharesBannerAdmin(admin.ModelAdmin):
    list_display = ['gallery_banner', 'url_banner', 'speed_banner']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['gallery_banner', 'url_banner', 'speed_banner']
    # readonly_fields = ['create_time', 'update_time']


class BackgroundBannerAdmin(admin.ModelAdmin):
    list_display = ['gallery_banner']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['gallery_banner']
    # readonly_fields = ['create_time', 'update_time']


class ContextAdvertiseAdmin(admin.ModelAdmin):
    list_display = ['photo_context']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['photo_context']
    # readonly_fields = ['create_time', 'update_time']


class MobileApplicationAdmin(admin.ModelAdmin):
    list_display = ['name_application', 'description_application', 'gallery_application', 'url_application']
    search_fields = ['name_application']
    list_filter = []
    # list_editable = []
    fields = ['name_application', 'description_application', 'gallery_application', 'url_application']
    # readonly_fields = ['create_time', 'update_time']


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name_social', 'url_social']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['name_social', 'url_social']
    # readonly_fields = ['create_time', 'update_time']


class MailingTemplatesAdmin(admin.ModelAdmin):
    list_display = ['template_mailing']
    search_fields = []
    list_filter = []
    # list_editable = []
    fields = ['template_mailing']
    # readonly_fields = ['create_time', 'update_time']


admin.site.register(Pages, PagesAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(AboutCinemaPage, AboutCinemaPageAdmin)
admin.site.register(NewsPage, NewsPageAdmin)
admin.site.register(SharesPage, SharesPageAdmin)
admin.site.register(CafeBarPage, CafeBarPageAdmin)
admin.site.register(VipHallPage, VipHallPageAdmin)
admin.site.register(AdvertisePage, AdvertisePageAdmin)
admin.site.register(ChildrenRoomPage, ChildrenRoomPageAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(CustomPage, CustomPageAdmin)

admin.site.register(Banners, BannersAdmin)
admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(HomeNewsSharesBanner, HomeNewsSharesBannerAdmin)
admin.site.register(BackgroundBanner, BackgroundBannerAdmin)

admin.site.register(ContextAdvertise, ContextAdvertiseAdmin)
admin.site.register(MobileApplication, MobileApplicationAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(MailingTemplates, MailingTemplatesAdmin)
