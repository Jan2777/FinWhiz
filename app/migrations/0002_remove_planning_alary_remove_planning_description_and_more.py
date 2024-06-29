# Generated by Django 5.0.6 on 2024-06-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planning',
            name='alary',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='description',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='title',
        ),
        migrations.AddField(
            model_name='planning',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
