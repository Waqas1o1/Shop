# Generated by Django 3.0.6 on 2020-07-16 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0039_auto_20200716_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 18, 25, 4, 942677)),
        ),
    ]
