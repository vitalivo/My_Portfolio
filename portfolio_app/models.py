# models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField()
    github_url = models.URLField()

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()