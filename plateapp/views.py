from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
  return render(request, 'restaurant/home.html')