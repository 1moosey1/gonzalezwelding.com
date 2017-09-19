import re
from django.conf import settings
from django.http import HttpResponseRedirect


# Requires three settings
# LOGIN_URL            - the url of the view to use
# EXEMPT_LOGIN_URLS    - the urls that are exempt from log in requirements
# REQUIRED_LOGIN_URLS  - the urls that require authentication
class RequireLoginMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response
        self.login_url = getattr(settings, 'LOGIN_URL', '/admin/login/')
        self.exempt_urls = tuple(re.compile(exempt_url) for exempt_url in settings.EXEMPT_LOGIN_URLS)
        self.required_urls = tuple(re.compile(required_url) for required_url in settings.REQUIRED_LOGIN_URLS)

    def __call__(self, request):

        response = self.process_request(request)

        if not response:
            return self.get_response(request)

        return response

    def process_request(self, request):

        if not request.user.is_authenticated:

            for url in self.exempt_urls:
                if url.match(request.path):
                    return None

            for url in self.required_urls:
                if url.match(request.path):
                    return HttpResponseRedirect('%s?next=%s' % (self.login_url, request.path))
