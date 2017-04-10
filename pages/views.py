from django.views.generic import TemplateView, RedirectView
from django.contrib import messages
from django.shortcuts import render
from pages.forms import ContactForm
from pages.models import Testimonial, Project

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

    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            cleaned_data = contact_form.cleaned_data
            messages.add_message(request, messages.INFO, 'Message Received')
            # TODO
            # Setup email server and send message

    else:
        contact_form = ContactForm()

    context = {'form': contact_form}
    return render(request, 'pages/contact.html', context)


# Render work page
def work(request):

    context = {'projects': Project.objects.all()}
    return render(request, 'pages/work.html', context)


# Render testimonials page
def testimonials(request):

    context = {'testimonials': Testimonial.objects.filter(display=True)}
    return render(request, 'pages/testimonials.html', context)
