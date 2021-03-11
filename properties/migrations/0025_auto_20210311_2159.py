# Generated by Django 3.1.2 on 2021-03-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0024_auto_20210311_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='youtube_video',
        ),
        migrations.AddField(
            model_name='property',
            name='youtube_id',
            field=models.CharField(blank=True, help_text='requires the id of youtube videoNot the full url.Id is the last part of the url eg.https://www.youtube.com/watch?v=ZIOCKqk4x3Athe id here isZIOCKqk4x3A', max_length=1024, null=True),
        ),
    ]
