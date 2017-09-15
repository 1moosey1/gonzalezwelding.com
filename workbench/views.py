from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from workbench.forms import LoginForm


# Render workbench home
def workbench(request):
    return render(request, 'workbench/home.html')


# Login page
def login_view(request):

    if request.POST:

        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:

                login(request, user)
                redirect_url = request.GET.get('next', '/workbench/')

                return HttpResponseRedirect(redirect_url)

            messages.error(request, 'Invalid username and/or password')

    else:
        login_form = LoginForm()

    context = {'form': login_form}
    return render(request, 'workbench/login.html', context)


# Logout view
def logout_view(request):

    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect(reverse('workbench:login'))
