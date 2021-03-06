# Generated by Django 3.0.6 on 2020-07-16 13:25

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0035_auto_20200716_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_cover',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[470, 620], upload_to=''),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='promtion_cover1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[1920, 728], upload_to=''),
        ),
    ]
