# Generated by Django 4.1.4 on 2022-12-17 16:45

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0021_alter_joinedevent_event_alter_joinedevent_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(verbose_name='Event Date & Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
    ]