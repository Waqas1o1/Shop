# Generated by Django 3.0.6 on 2020-07-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0029_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='Home.Tag'),
        ),
    ]
