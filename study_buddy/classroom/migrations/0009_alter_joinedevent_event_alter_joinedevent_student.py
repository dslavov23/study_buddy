# Generated by Django 4.1.4 on 2022-12-14 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import study_buddy.classroom.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0008_joinedevent'),
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
            field=models.ForeignKey(default=study_buddy.classroom.models.logged_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
