from django.urls import path
from client.views import index

urlpatterns = [
    path('', index),
]
