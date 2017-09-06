from django.http import HttpResponseRedirect


# Use redirect 303 as stated by specification
class HttpResponseSeeOther(HttpResponseRedirect):
    status_code = 303
