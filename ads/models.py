from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2500)
    address = models.CharField(max_length=2500)
    is_published = models.BooleanField(default=True)


class Categories(models.Model):
    name = models.CharField(max_length=100)
