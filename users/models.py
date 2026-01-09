from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = CloudinaryField('profile_images/')

    def __str__(self):
        return self.username

class About(models.Model):
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    email = models.EmailField()
    about_text = models.TextField()

class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=355)
    message = models.TextField()

    def __str__(self):
        return self.name + " " + self.subject

class TopHeader1(models.Model):
    message = models.CharField(max_length=350)

    def __str__(self):
        return self.message

class TopHeader2(models.Model):
    message = models.CharField(max_length=350)

    def __str__(self):
        return self.message

class HeroSectionButton(models.Model):
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.button_text