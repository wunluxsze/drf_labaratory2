from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Acter(models.Model):
    name = models.CharField(max_length=200)
    old = models.IntegerField()
    description = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)


class Films(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    data = models.DateField()
    country = models.CharField(max_length=200)
    acter = models.ManyToManyField(Acter)
    genre = models.ManyToManyField(Genre)
    category = models.ManyToManyField(Category)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.CharField(max_length=200)
    film = models.ForeignKey(Films, on_delete=models.CASCADE)


