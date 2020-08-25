
from django.contrib import admin
from django.urls import path
from .views import helloworld, hellocareeria

urlpatterns = [
    path('world/',helloworld),
    path('careeria/',hellocareeria)
]
