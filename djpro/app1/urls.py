from django.urls import path, re_path
from app1 import views

urlpatterns = [
    path('login', views.login),
    re_path('index/(\d+)', views.index),
]
