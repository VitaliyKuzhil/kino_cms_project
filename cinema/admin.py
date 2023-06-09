from django.contrib import admin
from .models import Seo, Gallery, Photos, Cinemas, Halls, Rows, Seats, Movies


class SeoAdmin(admin.ModelAdmin):
    list_display = ['url_seo', 'title_seo', 'keywords_seo', 'description_seo']
    search_fields = ['title_seo']
    list_filter = ['keywords_seo']
    # list_editable = []
    fields = ['url_seo', 'title_seo', 'keywords_seo', 'description_seo']
    # readonly_fields = ['create_time', 'update_time']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name_gallery']
    search_fields = ['name_gallery']
    list_filter = []
    # list_editable = []
    fields = ['name_gallery']
    # readonly_fields = ['create_time', 'update_time']


class PhotosAdmin(admin.ModelAdmin):
    list_display = ['photo']
    search_fields = ['gallery']
    list_filter = ['gallery']
    # list_editable = []
    fields = ['photo']
    # readonly_fields = ['create_time', 'update_time']


class CinemasAdmin(admin.ModelAdmin):
    list_display = ['name_cinema', 'description_cinema', 'logo_cinema', 'main_foto_cinema', 'amenities_cinema', 'gallery_cinema',
                    'seo_cinema', 'data_create_cinema']
    search_fields = ['name_cinema']
    list_filter = ['amenities_cinema', 'data_create_cinema']
    # list_editable = []
    fields = ['name_cinema', 'description_cinema', 'logo_cinema', 'amenities_cinema', 'gallery_cinema',
              'seo_cinema']
    # readonly_fields = ['create_time', 'update_time']


class HallsAdmin(admin.ModelAdmin):
    list_display = ['cinema_hall', 'number_hall', 'description_hall', 'photo_shem_hall', 'main_foto_hall',
                    'count_seats_hall', 'gallery_hall', 'seo_hall', 'data_create_hall']
    search_fields = ['cinema_hall', 'number_hall']
    list_filter = ['count_seats_hall', 'data_create_hall']
    # list_editable = []
    fields = ['cinema_hall', 'number_hall', 'description_hall', 'photo_shem_hall', 'main_foto_hall',
              'count_seats_hall', 'gallery_hall', 'seo_hall']
    # readonly_fields = ['create_time', 'update_time']


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['name_movie', 'description_movie', 'type_movie', 'main_foto_movie', 'status_movie',
                    'url_movie', 'gallery_movie', 'seo_movie', 'data_create_movie']
    search_fields = ['name_movie']
    list_filter = ['type_movie', 'status_movie', 'data_create_movie']
    # list_editable = []
    fields = ['name_movie', 'description_movie', 'type_movie', 'main_foto_movie', 'status_movie',
              'url_movie', 'gallery_movie', 'seo_movie']
    # readonly_fields = ['create_time', 'update_time']


admin.site.register(Seo, SeoAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Cinemas, CinemasAdmin)
admin.site.register(Halls, HallsAdmin)
admin.site.register(Movies, MoviesAdmin)


