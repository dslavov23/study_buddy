# Generated by Django 4.1.4 on 2022-12-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='grade',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]