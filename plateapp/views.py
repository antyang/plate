from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from plateapp.forms import UserForm, RestaurantForm
from django.contrib.auth import authenticate, login

# User model of django
from django.contrib.auth.models import User

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

  # when users submit data
  if request.method == "POST":
    user_form = UserForm(request.POST)
    restaurant_form = RestaurantForm(request.POST, request.FILES)

    if user_form.is_valid() and restaurant_form.is_valid():
      # create a new User object
      # give me clean data and transform to python type
      new_user = User.objects.create_user(**user_form.cleaned_data)
      # commit=False, hold onto new obj in memory, not to db yet
      new_restaurant = restaurant_form.save(commit=False)
      new_restaurant.user = new_user
      # now save to db
      new_restaurant.save()

      # login fn
      login(request, authenticate(
        username = user_form.cleaned_data["username"],
        password = user_form.cleaned_data["password"]
      ))

      return redirect(restaurant_home)

  # how do we pass in the forms to the frontend
  return render(request, 'restaurant/sign_up.html', {
    # here we pass in the forms
    "user_form": user_form,
    "restaurant_form": restaurant_form
    })


