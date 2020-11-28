from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TimeAbstractModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Platform(TimeAbstractModel):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)


class Category(models.Model):
    desc = models.CharField(max_length=256)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=128)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    category = models.ManyToManyField(Category)