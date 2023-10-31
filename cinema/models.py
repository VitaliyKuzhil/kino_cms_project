from django.core.validators import MinLengthValidator
from django.db import models
from .constants import StatusMovieChoices, TypeMovieChoices
from core.untils.cinema_validator import SeoValidator, MovieValidator
from core.untils.universal_validator import PhotoValidatorMixin, UrlValidatorMixin, CounterValidatorMixin


class Seo(models.Model, UrlValidatorMixin):  # Model SEO
    url_seo = models.URLField(null=True, blank=True, help_text='Input url address SEO')
    title_seo = models.CharField(validators=[MinLengthValidator(1)], max_length=300, help_text='Input title SEO')
    keywords_seo = models.CharField(null=True, blank=True, max_length=400, validators=[SeoValidator.validate_keywords],
                                    help_text='Input keywords SEO')
    description_seo = models.TextField(null=True, blank=True, help_text='Input description SEO')

    def __str__(self):
        return f'{self.title_seo}'

    def clean(self):
        super().clean()
        self.validate_url(self.url_seo)


class Gallery(models.Model):  # Model Gallery
    name_gallery = models.CharField(validators=[MinLengthValidator(1)], max_length=300, help_text='Input name Gallery')

    def __str__(self):
        return f'{self.name_gallery}'

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'gallerys'


class Photos(models.Model, PhotoValidatorMixin):  # Model Photo
    gallery = models.ManyToManyField(Gallery, through='GalleryPhotos', help_text='Select Gallery')
    photo = models.ImageField(blank=True, null=True, upload_to='static/photos/',
                              help_text='Upload an image. Supported formats: JPEG, PNG')

    def __str__(self):
        return f'{self.photo.name}'

    def clean(self):
        super().clean()
        self.validate_file_extension(self.photo)
        self.validate_file_size(self.photo)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class GalleryPhotos(models.Model):  # Connection ManyToMany between Gallery and Photos
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photos = models.ForeignKey(Photos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.gallery} {self.photos}'

    class Meta:
        verbose_name = 'gallery_photo'
        verbose_name_plural = 'gallery_photos'


class Cinemas(models.Model, PhotoValidatorMixin):  # Model Cinemas
    name_cinema = models.CharField(validators=[MinLengthValidator(1)], max_length=300, help_text='Input name Cinema')
    description_cinema = models.TextField(null=True, blank=True, help_text='Input description Cinema')
    logo_cinema = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                    help_text='Upload an image. Supported formats: JPEG, PNG')
    main_foto_cinema = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                         help_text='Upload an image. Supported formats: JPEG, PNG')
    amenities_cinema = models.TextField(null=True, blank=True, help_text='Input amenities Cinema')
    gallery_cinema = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                          help_text='Select Gallery')
    seo_cinema = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True,
                                      help_text='Select SEO')
    data_create_cinema = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.logo_cinema)
        self.validate_file_extension(self.main_foto_cinema)
        self.validate_file_size(self.logo_cinema)
        self.validate_file_size(self.main_foto_cinema)

    def __str__(self):
        return f'{self.name_cinema}'

    class Meta:
        verbose_name = 'cinema'
        verbose_name_plural = 'cinemas'
        ordering = ['name_cinema']


class Halls(models.Model, PhotoValidatorMixin, CounterValidatorMixin):  # Model Halls
    cinema_hall = models.ForeignKey(Cinemas, on_delete=models.CASCADE, help_text='Select Cinema to Hall')
    number_hall = models.IntegerField(default=1, help_text='Input number hall')
    description_hall = models.TextField(null=True, blank=True, help_text='Input description hall')
    photo_shem_hall = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                        help_text='Upload an image. Supported formats: JPEG, PNG')
    main_foto_hall = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                       help_text='Upload an image. Supported formats: JPEG, PNG')
    count_seats_hall = models.IntegerField(default=1, blank=True, null=True, help_text='Input count seats into hall')
    gallery_hall = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                        help_text='Select Gallery')
    seo_hall = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True,
                                    help_text='Select SEO')
    data_create_hall = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.photo_shem_hall)
        self.validate_file_extension(self.main_foto_hall)
        self.validate_file_size(self.photo_shem_hall)
        self.validate_file_size(self.main_foto_hall)
        self.count_integer(self.number_hall)
        self.count_integer(self.count_seats_hall)

    def __str__(self):
        return f'{self.number_hall}'

    class Meta:
        verbose_name = 'hall'
        verbose_name_plural = 'halls'
        ordering = ['number_hall']


class Rows(models.Model):  # Model Rows
    row_hall = models.ForeignKey(Halls, on_delete=models.CASCADE,
                                 help_text='Select Hall to Row')  # Connection ForeignKey between Halls and Rows
    number_row = models.PositiveIntegerField(default=1, help_text='Input number row into hall')

    class Meta:
        verbose_name = 'row'
        verbose_name_plural = 'rows'

    def __str__(self):
        return f'{self.number_row}'


class Seats(models.Model):  # Model Seats
    seat_row = models.ManyToManyField(Rows, through='SeatsRows', help_text='Select Row to Seat')
    number_seat = models.PositiveIntegerField(default=1, unique=True, help_text='Input number seat into row')

    class Meta:
        verbose_name = 'seat'
        verbose_name_plural = 'seats'

    def __str__(self):
        return f'{self.number_seat}'


class SeatsRows(models.Model):  # Relation between Rows and Seats model
    row = models.ForeignKey(Rows, on_delete=models.CASCADE, help_text='row')
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE, help_text='seat')
    status_seat = models.BooleanField(default=False, help_text='Select status Seat')

    def __str__(self):
        return f'{self.row} {self.seat}'

    class Meta:
        verbose_name = 'seat_in_row'
        verbose_name_plural = 'seats_in_row'
        unique_together = [['row', 'seat']]


class Movies(models.Model, PhotoValidatorMixin, UrlValidatorMixin):  # Model Movies
    name_movie = models.CharField(validators=[MinLengthValidator(1)], max_length=300, help_text='Input name Movie')
    description_movie = models.TextField(null=True, blank=True, help_text='Input description Movie')
    type_movie = models.CharField(choices=TypeMovieChoices.choices, validators=[MovieValidator.validate_check_type],
                                  help_text='Check type Movie')
    main_foto_movie = models.ImageField(upload_to='static/photos/', null=True, blank=True,
                                        help_text='Upload an image. Supported formats: JPEG, PNG')
    status_movie = models.CharField(null=True, blank=True,
                                    choices=StatusMovieChoices.choices, default=StatusMovieChoices.SOON,
                                    help_text='Select status Movie')
    url_movie = models.URLField(max_length=300, null=True, blank=True, help_text='Input url Movie')
    gallery_movie = models.OneToOneField(Gallery, on_delete=models.CASCADE, null=True, blank=True,
                                         help_text='Select Gallery')
    seo_movie = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True,
                                     help_text='Select SEO')
    data_create_movie = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        self.validate_file_extension(self.main_foto_movie)
        self.validate_file_size(self.main_foto_movie)
        self.validate_url(self.url_movie)

    def __str__(self):
        return f'{self.name_movie}'

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
        ordering = ['name_movie']
