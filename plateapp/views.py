from django.shortcuts import render

# Create your views here.

# views.py acts like a controller
# containing fn act like actions

# Create function name home, that redirects users to home page
def home(request):
  return render(request, 'home.html', {})
