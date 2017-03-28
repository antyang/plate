from django.db import models
from django.contrib.auth.models import User

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