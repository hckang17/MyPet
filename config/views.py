from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def welcome_page(request):
    return render(request, 'welcome_page.html')

