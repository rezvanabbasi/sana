from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile',
        null=True
    )
    role = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='role',
        null=True
    )
    password = models.CharField(max_length=150, null=True)
    mobile = models.CharField(max_length=20, null=True)
    national_code = models.CharField(max_length=15, null=True)
    province = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.national_code


class Reception(models.Model):
    title = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    time = models.CharField(max_length=50, null=True)
    doctor = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='reception',
        null=True
    )
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UserReception(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='user_reception'
    )
    reception = models.ForeignKey(
        Reception,
        on_delete=models.CASCADE,
        related_name='user_reception'
    )
    reason = models.TextField(null=True)

    def __str__(self):
        return self.reception.title


class Visit(models.Model):
    reception = models.OneToOneField(
        UserReception,
        on_delete=models.CASCADE,
        null=True
    )
    result = models.TextField(null=True)

    def __str__(self):
        return self.reception.reception_id