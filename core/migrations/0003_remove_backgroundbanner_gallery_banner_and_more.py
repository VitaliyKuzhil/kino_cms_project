# Generated by Django 4.2.1 on 2023-10-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_custompage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundbanner',
            name='gallery_banner',
        ),
        migrations.AddField(
            model_name='backgroundbanner',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Upload an image. Supported formats: JPEG, PNG', null=True, upload_to='static/photos/'),
        ),
    ]