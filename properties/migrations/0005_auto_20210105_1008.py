# Generated by Django 3.1.2 on 2021-01-05 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20201110_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='size',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
