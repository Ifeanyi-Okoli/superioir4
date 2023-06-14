from django.contrib.auth.backends import ModelBackend

class CustomAuthenticationBackend(ModelBackend):
    def user_can_authenticate(self, user):
        """
        Allow all users to authenticate, regardless of password validation.
        """
        return True
