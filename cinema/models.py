from django.db import models


class Seo(models.Model):  # Model SEO
    id_seo = models.AutoField(primary_key=True)
    url_seo = models.URLField(max_length=300, null=True, blank=True)
    title_seo = models.CharField(max_length=300, null=False, blank=False)
    keywords_seo = models.CharField(max_length=400, null=False, blank=False)
    description_seo = models.TextField(null=True, blank=True)


class Gallery(models.Model):  # Model Gallery
    id_gallery = models.AutoField(primary_key=True)
    name_gallery = models.CharField(max_length=300, null=False, blank=False, unique=True)


class Photos(models.Model):  # Model Photo
    id_photo = models.AutoField(primary_key=True)
    gallery = models.ManyToManyField(Gallery, through='GalleryPhotos', null=True, blank=True)
    photo = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False)


class GalleryPhotos(models.Model):  # Connection ManyToMany between Gallery and Photos
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photos = models.ForeignKey(Photos, on_delete=models.CASCADE)


class Cinemas(models.Model):  # Model Cinemas
    id_cinema = models.AutoField(primary_key=True)
    name_cinema = models.CharField(max_length=300, null=False, blank=False)
    description_cinema = models.TextField(null=True, blank=True)
    logo_cinema = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    main_foto_cinema = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    amenities_cinema = models.CharField(max_length=500, null=True, blank=True)
    gallery_cinema = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    seo_cinema = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)
    data_create_cinema = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'Cinema: {self.name_cinema}'

    class Meta:
        verbose_name = 'Cinema'
        verbose_name_plural = 'Cinemas'
        ordering = ['name_cinema']


class Halls(models.Model):  # Model Halls
    id_hall = models.AutoField(primary_key=True)
    cinema_hall = models.ForeignKey(Cinemas, on_delete=models.CASCADE, blank=False, null=False)
    number_hall = models.IntegerField(default=1, blank=False, null=False)
    description_hall = models.TextField(null=True, blank=True)
    photo_shem_hall = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    main_foto_hall = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    count_seats_hall = models.IntegerField(default=1, blank=True, null=True)
    gallery_hall = models.OneToOneField(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    seo_hall = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)
    data_create_hall = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f'Hall: {self.number_hall}'

    class Meta:
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls'
        ordering = ['number_hall']


class Rows(models.Model):  # Model Rows
    id_row = models.AutoField(primary_key=True)
    row_hall = models.ForeignKey(Halls, on_delete=models.CASCADE, blank=False,
                                 null=False)  # Connection ForeignKey between Halls and Rows


class Seats(models.Model):  # Model Seats
    id_seat = models.AutoField(primary_key=True)
    seat_row = models.ManyToManyField(Rows, through='SeatsRows', null=False, blank=False)
    status_seat = models.BooleanField(default=False, blank=True, null=True)


class SeatsRows(models.Model):  # Connection ManyToMany between Rows and Seats
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE)
    row = models.ForeignKey(Rows, on_delete=models.CASCADE)


class Movies(models.Model):  # Model Movies
    id_movie = models.AutoField(primary_key=True)
    name_movie = models.CharField(max_length=300, null=False, blank=False)
    description_movie = models.TextField(null=True, blank=True)
    type_movie = models.CharField(max_length=70, null=False, blank=False)
    main_foto_movie = models.ImageField(upload_to='static/photos/%Y/%m/%d/', editable=False, null=True, blank=True)
    status_movie = models.CharField(max_length=50, null=True, blank=True)
    url_movie = models.URLField(max_length=300, null=True, blank=True)
    gallery_movie = models.OneToOneField(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    seo_movie = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True)
    data_create_movie = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'Movie: {self.name_movie}'

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['name_movie']
