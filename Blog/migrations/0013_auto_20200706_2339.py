# Generated by Django 3.0.6 on 2020-07-06 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_auto_20200701_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 23, 39, 47, 458045)),
        ),
    ]
