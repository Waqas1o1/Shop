# Generated by Django 3.0.6 on 2020-07-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0025_auto_20200707_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupen',
            name='expire_date',
            field=models.DateTimeField(),
        ),
    ]
