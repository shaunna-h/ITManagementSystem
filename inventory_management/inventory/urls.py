# creating a url to point to the index page
# similar to the one in inventory_management, but created this one for ease also

from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', user_logout, name='logout'),
]