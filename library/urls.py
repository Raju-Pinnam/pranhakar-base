from django.urls import path

from library.views import *

urlpatterns = [
    path('', dummy_fun)
]