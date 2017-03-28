from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from plateapp.forms import UserForm, RestaurantForm

# Create your views here.

# views.py acts like a controller
# containing fn act like actions

# Create function name home, that redirects users to home page
def home(request):
  # redirect is a fn from django
  return redirect(restaurant_home)
  # return render(request, 'home.html', {})

# here we're checking authetication of the user
# if authenticated run fn, otherwise go to login_url
@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
  return render(request, 'restaurant/home.html', {})

# sign-up fn
def restaurant_sign_up(request):
  user_form = UserForm()
  restaurant_form = RestaurantForm()
  # how do we pass in the forms to the frontend
  return render(request, 'restaurant/sign_up.html', {
    # here we pass in the forms
    "user_form": user_form,
    "restaurant_form": restaurant_form
    })