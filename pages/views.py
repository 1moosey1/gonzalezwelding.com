from django.shortcuts import render, redirect
from django.http import HttpResponse


# Index view redirects to home page
def index(request):
    return redirect('home')


# Render home page
def home(request):
    return render(request, 'pages/index.html')
