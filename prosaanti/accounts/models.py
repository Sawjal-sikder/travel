from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
