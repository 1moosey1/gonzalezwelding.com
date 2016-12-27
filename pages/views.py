from django.views.generic import TemplateView, RedirectView
from django.contrib import messages
from django.shortcuts import render
from pages.forms import ContactForm

import os


# Index View - redirects to home page
class IndexView(RedirectView):

    permanent = True
    query_string = False
    pattern_name = 'pages:home'


# Home View - render home page
class HomeView(TemplateView):
    template_name = 'pages/index.html'


# About View - render about page
class AboutView(TemplateView):
    template_name = 'pages/about.html'


# Render contact page
def contact(request):

    api_key = os.environ['GMAPKEY']
    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            cleaned_data = contact_form.cleaned_data
            messages.add_message(request, messages.INFO, 'Message Received')
            # TODO
            # Setup email server and send message

    else:
        contact_form = ContactForm()

    context = {'form': contact_form, 'api_key': api_key}
    return render(request, 'pages/contact.html', context)


# Render Testimonials
def testimonials(request):
    return render(request, 'pages/testimonials.html')
