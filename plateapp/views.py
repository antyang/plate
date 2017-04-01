from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from plateapp.forms import UserForm, RestaurantForm, UserFormForEdit, MealForm
from django.contrib.auth import authenticate, login

# User model of django
from django.contrib.auth.models import User
from plateapp.models import Meal, Order, OrderDetails


# Create your views here.

# views.py acts like a controller
# containing fn act like actions
# getting and handling data

# Create function name home, that redirects users to home page
def home(request):
  # redirect is a fn from django
  return redirect(restaurant_home)
  # return render(request, 'home.html', {})

# here we're checking authetication of the user
# if authenticated run fn, otherwise go to login_url
@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
  # return render(request, 'restaurant/base.html', {})
  return redirect(restaurant_order)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_account(request):

  # allow user editing
  user_form = UserFormForEdit(instance = request.user)
  restaurant_form = RestaurantForm(instance = request.user.restaurant)

  # update
  if request.method == "POST":
    user_form = UserFormForEdit(request.POST, instance = request.user)
    restaurant_form = RestaurantForm(request.POST, request.FILES, instance = request.user.restaurant)

    if user_form.is_valid() and restaurant_form.is_valid():
      user_form.save()
      restaurant_form.save()

  return render(request, 'restaurant/account.html', {
      "user_form": user_form,
      "restaurant_form": restaurant_form
    })

@login_required(login_url='/restaurant/sign-in/')
def restaurant_meal(request):
  # get all the meals with this condition
  meals = Meal.objects.filter(restaurant = request.user.restaurant).order_by("-id")
  return render(request, 'restaurant/meal.html', {
    "meals": meals
    })

@login_required(login_url='/restaurant/sign-in/')
def restaurant_add_meal(request):
  form = MealForm()

  if request.method == "POST":
    # set form
    form = MealForm(request.POST, request.FILES)

    if form.is_valid():
      # create meal obj, don't save in db yet
      meal = form.save(commit=False)
      # set to users restaurant
      meal.restaurant = request.user.restaurant
      # then save to db
      meal.save()
      return redirect(restaurant_meal)

  return render(request, 'restaurant/add_meal.html', {
    # render above defined "form" to front page
    "form": form
    })

@login_required(login_url='/restaurant/sign-in/')
def restaurant_edit_meal(request, meal_id):
  # get meals from db based on ID
  form = MealForm(instance = Meal.objects.get(id = meal_id))

  if request.method == "POST":
    # set form
    form = MealForm(request.POST, request.FILES, instance = Meal.objects.get(id = meal_id))

    if form.is_valid():
      form.save()
      return redirect(restaurant_meal)

  return render(request, 'restaurant/edit_meal.html', {
    # render above defined "form" to front page
    "form": form
    })


@login_required(login_url='/restaurant/sign-in/')
def restaurant_order(request):
  if request.method == "POST":
    order = Order.objects.get(id = request.POST["id"], restaurant = request.user.restaurant)

    if order.status == Order.COOKING:
      order.status = Order.READY
      order.save()

  orders = Order.objects.filter(restaurant = request.user.restaurant).order_by("-id")
  return render(request, 'restaurant/order.html', {
    "orders": orders
    })

@login_required(login_url='/restaurant/sign-in/')
def restaurant_report(request):
  return render(request, 'restaurant/report.html', {})


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


