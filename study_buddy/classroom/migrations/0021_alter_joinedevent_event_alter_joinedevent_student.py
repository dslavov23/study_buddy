# Generated by Django 4.1.4 on 2022-12-17 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0020_location_delete_homework_remove_event_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinedevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.event'),
        ),
        migrations.AlterField(
            model_name='joinedevent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
