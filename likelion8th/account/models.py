from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER = (
        ("M", "남자"),
        ("F", "여자"),
    )
    nickname = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True, choices=GENDER)
    phone = models.IntegerField(blank=True, null=True, help_text="(only number)")
   