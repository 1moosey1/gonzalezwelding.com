from django.shortcuts import render, redirect
from django.http import HttpResponse


# Index view redirects to home page
def index(request):
    return redirect('pages:home')


# Render home page
def home(request):
    return render(request, 'pages/index.html')


# Render about page
def about(request):
    return render(request, 'pages/about.html')
