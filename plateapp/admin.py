from django.contrib import admin

# Register your models here.

# import Restaurant form models
from plateapp.models import Restaurant, Customer, Driver, Meal

# add Models obj to the admin site
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)

# everytime we make changes to model we need to django migrate changes to db
# makemigrations
# migrate
# re-run server