# Generated by Django 3.1.2 on 2021-01-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_auto_20210119_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
