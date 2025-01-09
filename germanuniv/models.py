from django.contrib.auth.models import AbstractUser
from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    semester_fee = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=255)

class User(AbstractUser):
    nickname = models.CharField(max_length=255, blank=True, null=True)
    favorite_school = models.ManyToManyField(School, related_name='favorited_by')  # 다대다 관계 추가

class Residence(models.Model):
    id = models.AutoField(primary_key=True)
    residence_type = models.CharField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='residences')

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='languages')