# Generated by Django 4.1.4 on 2022-12-16 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0018_comment_user_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.CharField(max_length=150, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_c',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]