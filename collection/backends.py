from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    success_url = 'registration_create_thing'