from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


class Confirm_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code