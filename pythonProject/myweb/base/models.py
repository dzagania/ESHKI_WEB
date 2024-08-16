from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class Style(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class Eshkhi(models.Model):
    style = models.ManyToManyField(Style, blank=True, related_name="eshkhi")
    color = models.CharField(max_length=300)
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=200)
    matter = models.CharField(max_length=200)


class Meta:
    ordering = ['color']

    def __str__(self):
        return f"{self.color} _ {self.matter}"


class User(AbstractUser):
    clothes = models.ManyToManyField(Eshkhi, blank=True, related_name="users")
    avatar = models.ImageField(null=True, default='avatar.svg')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Eshkhi, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body


class Animal(models.Model):
    name = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)

    def speak(self):
        return f'The {self.name} says "{self.sound}" '

    def __str__(self):
        return self.name
