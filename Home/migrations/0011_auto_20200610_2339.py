# Generated by Django 3.0.6 on 2020-06-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_promotions_promotion_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_cover',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_publishDate',
            field=models.DateTimeField(default=''),
        ),
    ]
