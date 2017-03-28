from django.contrib import admin

# Register your models here.

# import Restaurant form models
from plateapp.models import Restaurant

# add Restaurant obj to the admin site
admin.site.register(Restaurant)