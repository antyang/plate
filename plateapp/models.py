from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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

class Order(models.Model):
  COOKING = 1
  READY = 2
  ONTHEWAY = 3
  DELIEVERED = 4

  STATUS_CHOICES = (
    (COOKING, "Cooking"),
    (READY, "Ready"),
    (ONTHEWAY, "On The Way"),
    (DELIEVERED, "Delievereds"),
  )

  # We need information on Customer, Restaurant, Driver
  customer = models.ForeignKey(Customer)
  restaurant = models.ForeignKey(Restaurant)
  driver = models.ForeignKey(Driver)

  address = models.CharField(max_length=500)
  total = models.IntegerField()
  status = models.IntegerField(choices = STATUS_CHOICES)
  create_at = models.DateTimeField(default = timezone.now)
  picked_at = models.DateTimeField(blank = True, null = True)

  def __str__(self):
    return str(self.id)

class OrderDetails(models.Model):
  order = models.ForeignKey(Order, related_name='order_details')
  # linking to meal
  meal = models.ForeignKey(Meal)
  quantity = models.IntegerField()
  sub_total = models.IntegerField()

  def __str__(self):
    return str(self.id)




