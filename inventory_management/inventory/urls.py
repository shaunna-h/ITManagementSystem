# creating a url to point to the index page
# similar to the one in inventory_management, but created this one for ease also

from django.contrib import admin
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]