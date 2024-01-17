from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import response, status

from library.models import Book

@api_view(['GET'])
def dummy_fun(request):
    qs = Book.objects.count()
    return response.Response(
        f"Hi This is calling {qs}", status=status.HTTP_200_OK
    )

# func
# class


