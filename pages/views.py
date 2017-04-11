from django.views.generic import TemplateView, RedirectView
from django.contrib import messages
from django.shortcuts import render
from pages.forms import ContactForm
from pages.models import Testimonial, Project
from django.core.mail import send_mail
from django.views.decorators.clickjacking import xframe_options_exempt

# Index View - redirects to home page
class IndexView(RedirectView):

    permanent = True
    query_string = False
    pattern_name = 'pages:home'


# Home View - render home page
@xframe_options_exempt
def home(request):
    return render(request, 'pages/index.html')


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

    context = {'projects': Project.objects.all()}
    return render(request, 'pages/work.html', context)


# Render testimonials page
def testimonials(request):

    context = {'testimonials': Testimonial.objects.filter(display=True)}
    return render(request, 'pages/testimonials.html', context)
