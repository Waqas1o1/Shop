# Generated by Django 3.0.6 on 2020-06-11 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_auto_20200611_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_name', models.CharField(max_length=50, verbose_name='Name Of the Deal')),
                ('deal_desc', models.TextField()),
                ('deat_duration', models.TimeField(verbose_name='Duration Time')),
                ('deal_img', models.ImageField(upload_to='', verbose_name='Deal Of The Day Cover Image')),
                ('deal_catg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Product')),
            ],
        ),
    ]
