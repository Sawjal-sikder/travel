from django.urls import path
from .views import *

urlpatterns = [
    path('', adminPanel, name='admin')
]
