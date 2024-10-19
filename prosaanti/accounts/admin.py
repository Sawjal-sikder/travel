from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(userProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone')
