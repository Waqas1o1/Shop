# Generated by Django 3.0.6 on 2020-07-13 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0023_auto_20200714_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 0, 53, 16, 886342)),
        ),
    ]