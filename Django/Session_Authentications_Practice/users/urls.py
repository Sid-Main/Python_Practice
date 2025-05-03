from django.urls import path, include
from django.contrib import admin
from .views import login_view, user_view, create_user

urlpatterns=[
    path('users/', user_view),
    path('register/', login_view),
    path("create/", create_user)
]