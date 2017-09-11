from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# 204 with a redirect url (303 not working for XmlHttpRequest DELETE)
class NoContentRedirect(HttpResponse):

    def __init__(self, location, *args, **kwargs):

        super(NoContentRedirect, self).__init__(*args, **kwargs)

        self.status_code = 204
        self['Location'] = location


# Use redirect 303 as stated by specification
class HttpResponseSeeOther(HttpResponseRedirect):
    status_code = 303


# Cleaner shortcut to use 404
def render404(request, message):
    return render(request, 'workbench/404.html', {'404message': message}, status=404)
