# Generated by Django 3.0.6 on 2020-07-16 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0035_auto_20200716_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 18, 9, 44, 744238)),
        ),
    ]
