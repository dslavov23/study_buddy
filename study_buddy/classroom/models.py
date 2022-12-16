from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model, get_user
from django.db import models
from django.contrib.auth.models import User
from study_buddy.members.models import AppUser, Profile

UserModel =  get_user_model()
# Create your models here.

class Homework(models.Model):
    subject = models.CharField(
        max_length=30,
    )
    homework_url = models.URLField()

    def __str__(self):
        return self.subject


class School(models.Model):
    name = models.CharField(
        max_length=40,
    )

    address = models.CharField(
        max_length=200,
    )

    post_code = models.CharField(
        max_length=10,
    )
    phone = models.CharField(
        max_length=20,
    )
    email_address = models.EmailField(
        'Email Address'
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    str_fields = ('photo',)
    name = models.CharField(
        'Event Name',
        max_length=40,

    )
    event_date = models.DateTimeField(
        'Event Date',
    )
    school = models.ForeignKey(
        School,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    teacher = models.CharField(
        max_length=40,
    )
    description = models.TextField(
        blank=True,
    )
    photo = CloudinaryField('photo')

    def __str__(self):
        return self.name


def logged_user(request):
    current_user = request.user
    return current_user


class JoinedEvent(models.Model):
    student = models.ForeignKey(AppUser, on_delete=models.RESTRICT)
    event = models.ForeignKey(Event, on_delete=models.RESTRICT)

class Comment(models.Model):
    description=models.CharField(max_length=50,)
    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    event_c = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    user_c = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
