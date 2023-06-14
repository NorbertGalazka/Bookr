from django.http import HttpResponse
from .models import Book
from django.shortcuts import render


def welcome_view(request):
    return render(request, 'base.html')
