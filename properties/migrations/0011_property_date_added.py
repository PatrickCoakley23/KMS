# Generated by Django 3.1.2 on 2021-01-19 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_auto_20210118_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
