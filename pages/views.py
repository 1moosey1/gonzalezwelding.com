from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.forms import ContactForm
import os


# Index view redirects to home page
def index(request):
    return redirect('pages:home')


# Render home page
def home(request):
    return render(request, 'pages/index.html')


# Render about page
def about(request):
    return render(request, 'pages/about.html')


# Render contact page
def contact(request):

    api_key = os.environ['GMAPKEY']
    message = None
    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            cleaned_data = contact_form.cleaned_data
            message = 'Message Received'
            # TODO
            # Setup email server and send message

    else:
        contact_form = ContactForm()

    context = {'form': contact_form, 'message': message, 'api_key': api_key}
    return render(request, 'pages/contact.html', context)
