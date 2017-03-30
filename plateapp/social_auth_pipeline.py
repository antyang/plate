from plateapp.models import Customer, Driver

def create_user_by_type(backend, user, request, response, *args, **kwargs):
  # if backend name is facebook, get facebook profile avatar image
  if backend.name == 'facebook':
    # append facebook id to string
    avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

    # IF user type is driver and drive does not exist in db, then create a new Driver
    # OTHERWISE create a new Customer only if customer does not exist in db
    if request['user_type'] == "driver" and not Driver.objects.filter(user_id=user.id):
      Driver.objects.create(user_id=user.id, avatar = avatar)
    elif not Customer.objects.filter(user_id=user.id):
      Customer.objects.create(user_id=user.id, avatar = avatar)