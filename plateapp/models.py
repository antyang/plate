from django.db import models
from django.contrib.auth.models import User
import logging

# Create your models here.

# OneToOne field:
  # restaurant belong to 1 owner, 1 owner only have 1 restaurant
# CASCADE:
  # once you delete user, you delete the restaurant as well
# to use ImageField, we need to install Pillow pkg
  # pip install pillow
class Restaurant(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
  name = models.CharField(max_length=500)
  phone = models.CharField(max_length=500)
  address = models.CharField(max_length=500)
  logo = models.ImageField(upload_to='restaurant_logo/', blank=False)

  # Turns Restaurant object => object.name => Restaurant
  def __str__(self):
    return self.name

    logger.info(logo)

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
  avatar = models.CharField(max_length=500)
  phone = models.CharField(max_length=500, blank=True)
  address = models.CharField(max_length=500, blank=True)

  def __str__(self):
    return self.user.get_full_name()
    # get_full_name fn is form User model of django
    # which returns a full name

class Driver(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
  avatar = models.CharField(max_length=500)
  phone = models.CharField(max_length=500, blank=True)
  address = models.CharField(max_length=500, blank=True)

  def __str__(self):
    return self.user.get_full_name()


class Meal(models.Model):
  # 1 rest can have many meals
  # 1 meal can only have 1 rest
  restaurant = models.ForeignKey(Restaurant)
  name = models.CharField(max_length=500)
  short_description = models.CharField(max_length=500)
  image = models.ImageField(upload_to='meal_images/', blank=False)
  price = models.IntegerField(default=0)

  def __str__(self):
    return self.name






