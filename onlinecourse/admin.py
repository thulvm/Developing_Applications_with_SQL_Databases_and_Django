from django.contrib import admin

# Register your models here.
from django.db import models

class Question(models.Model):
  content = models.CharField(max_length=255)

class Choice(models.Model):
  content = models.CharField(max_length=255)
