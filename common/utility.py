from math import ceil, floor
from django.conf import settings
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
def render404(request, message, html):

    context = {

        '404message': message
    }

    return render(request, html, context, status=404)


'''
Pagination shortcut/view
Renders the given html with a generic pagination context

Context:
- objects: the filter objects based on current page
- current_page: the page number sent through get parameter page
- page_range: the page numbers to link and display based on max display setting

Parameters:
- request: basic request
- object: the model to query and filter
- html: the html page to render
- html404: the html page to render upon 404
'''


def render_paginated(request, object, html, html404):

    # If no objects then render page with no context
    objects = object.objects.all()
    if not objects.exists():
        return render(request, html)

    # Parse page number
    page = request.GET.get('page', 0)

    try:
        page = abs(int(page))

    except ValueError:
        page = 0

    # If page is out of bounds render 404
    pages = ceil(len(objects) / settings.MAX_OBJECT_DISPLAY)
    if page >= pages:
        return render404(request, 'Page not found!', html404)

    context = {

        'objects': filter_objects(objects, page),
        'current_page': page,
        'page_range': create_prange(page, pages)
    }

    return render(request, html, context)


# Filter objects based on page and settings
def filter_objects(objects, current_page):

    # Filter projects based on current page
    offset = current_page * settings.MAX_OBJECT_DISPLAY
    limit = offset + settings.MAX_OBJECT_DISPLAY

    return objects[offset:limit]


# Determine the page range to display
# Uses MAX_DISPLAY and MAX_PAGE_RANGE settings
def create_prange(current_page, pages):

    max_range = settings.MAX_PAGE_RANGE
    lower_breakpoint = floor(max_range / 2)
    upper_breakpoint = lower_breakpoint + 1

    lower_bound = 0
    upper_bound = pages

    # Adjust the page range to display if more than 5 pages
    if pages > max_range:

        if current_page <= lower_breakpoint:
            upper_bound = max_range

        elif current_page >= pages - upper_breakpoint:
            lower_bound = pages - max_range

        else:

            lower_bound = current_page - lower_breakpoint
            upper_bound = current_page + upper_breakpoint

    page_range = []
    for i in range(lower_bound, upper_bound):
        page_range.append(i)

    return page_range

''' 
Old page range calculation - MAX: 5
# Determine the page range to display
# Displays odd page ranges
def create_prange(projects, current_page):

    pages = math.ceil(len(projects) / settings.MAX_PROJECT_DISPLAY)

    lower_bound = 0
    upper_bound = pages

    # Adjust the page range to display if more than 5 pages
    if pages > 5:

        if current_page <= 2:
            upper_bound = 5

        elif current_page >= pages - 3:
            lower_bound = pages - 5

        else:

            lower_bound = current_page - 2
            upper_bound = current_page + 3

    page_range = []
    for i in range(lower_bound, upper_bound):
        page_range.append(i)

    return page_range
'''
