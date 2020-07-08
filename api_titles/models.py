from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from api_user.models import User


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True, null=True, verbose_name='Жанр')
    category = models.ManyToManyField(Category, blank=True, null=True, verbose_name='Категория')

