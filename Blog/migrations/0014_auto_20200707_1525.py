# Generated by Django 3.0.6 on 2020-07-07 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_auto_20200706_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 15, 25, 46, 571923)),
        ),
    ]