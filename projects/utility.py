import math
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from projects.models import Project, Image


# Retrieve project if it exists
def get_project(project_id):

    try:
        project = Project.objects.get(id=project_id)

    except (ValueError, ObjectDoesNotExist):
        return False

    return project


# Handles creation of projects
def handle_project_creation(create_form):

    cleaned_data = create_form.cleaned_data
    files = create_form.files

    # Create new project and save it
    new_project = Project(title=cleaned_data['title'], description=cleaned_data['description'])
    new_project.save()

    # Save all uploaded images
    save_images(new_project, files.getlist('images'))


# Handles modification of projects
def handle_project_modification(mod_form):

    project = mod_form.project
    cleaned_data = mod_form.cleaned_data
    files = mod_form.files

    # Save project updates
    project.title = cleaned_data['title']
    project.description = cleaned_data['description']
    project.save()

    if files:
        save_images(project, files.getlist('images'))

    if cleaned_data['checkboxes']:
        delete_images(project, cleaned_data['checkboxes'])


# Handle deletion of projects
def handle_project_deletion(project):
    project.delete()


# Save uploaded images
def save_images(project, files):

    for file in files:

        uploaded_image = Image(image_field=file, project=project)
        uploaded_image.save()

        project.images.add(uploaded_image)


# Delete uploaded images
def delete_images(project, image_ids):

    for image_id in image_ids:

        image_id = int(image_id)
        image = project.images.get(id=image_id)
        image.delete()


# Generate project and page range context
def filter_projects(projects, current_page):

    # Filter projects based on current page
    offset = current_page * settings.MAX_PROJECT_DISPLAY
    limit = offset + settings.MAX_PROJECT_DISPLAY

    return projects[offset:limit]

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


# Determine the page range to display
# Uses MAX_DISPLAY and MAX_PAGE_RANGE settings
def create_prange(projects, current_page):

    pages = math.ceil(len(projects) / settings.MAX_PROJECT_DISPLAY)
    max_range = settings.MAX_PAGE_RANGE
    lower_breakpoint = math.floor(max_range / 2)
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
