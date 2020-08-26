
from django.contrib import admin
from django.urls import path
from .views import helloworld, hellocareeria, counter as c, increment, decrement, reset
urlpatterns = [
    path('world/',helloworld),
    path('careeria/',hellocareeria),
    path('counter/',c),
    path('increment/', increment),
    path('reset/', reset),
    path('decrement/', decrement)
]
