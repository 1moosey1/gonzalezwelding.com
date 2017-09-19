from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import RedirectView
from common.utility import render_paginated
from pages.forms import ContactForm
from projects.models import Project


# Index View - redirects to home page
class IndexView(RedirectView):

    permanent = True
    query_string = False
    pattern_name = 'pages:home'


# Render home page
def home(request):
    return render(request, 'pages/index.html')


# Render about page
def about(request):
    return render(request, 'pages/about.html')


# Render contact page
def contact(request):

    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            cleaned_data = contact_form.cleaned_data
            messages.add_message(request, messages.INFO, 'Message Received')

            email = 'gwm.assistant@gmail.com'
            message = 'Name: ' + cleaned_data['name'] + '\n' \
            + 'Subject: ' + cleaned_data['subject'] + '\n' \
            + 'Message: ' + cleaned_data['message']

            send_mail('Contact', message, email, [email])
            if cleaned_data['email']:

                message = 'Thank you for contacting GWM.' + '\n' \
                + 'Will get back to you ASAP!'
                send_mail('auto-reply', message, email, [cleaned_data['email']])

            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    context = {'form': contact_form}
    return render(request, 'pages/contact.html', context)


# Render work page
def work(request):
    return render_paginated(request, Project, 'pages/work.html', 'pages/404.html')


# Render testimonials page
def testimonials(request):
    return render(request, 'pages/testimonials.html')
