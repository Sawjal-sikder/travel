from django.urls import path
from .views import *

urlpatterns = [
    path('', adminPanel, name='admin'),
    path('settings/', comInfo, name='comInfo'),
    path('user/', clintList, name='clintList'),
    path('user/read/<int:id>/', read, name='read'),
]
