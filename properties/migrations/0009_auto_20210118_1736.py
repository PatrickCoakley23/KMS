# Generated by Django 3.1.2 on 2021-01-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_auto_20210108_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='ber_rating',
            field=models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('D1', 'D1'), ('D2', 'D2'), ('E1', 'E1'), ('E2', 'E2'), ('FG', 'FG'), ('Exempt', 'EXEMPT')], max_length=10, null=True),
        ),
    ]
