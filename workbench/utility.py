from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from workbench.models import Project, Image


# Use redirect 303 as stated by specification
class HttpResponseSeeOther(HttpResponseRedirect):
    status_code = 303


# Handles creation of projects
def handle_project_creation(create_form):

    # Shorten calls
    cleaned_data = create_form.cleaned_data
    files = create_form.files

    # Create new project and save it
    new_project = Project(title=cleaned_data['title'], description=cleaned_data['description'])
    new_project.save()

    # Get all uploaded images
    save_images(new_project, files.getlist('images'))

    return HttpResponseSeeOther(reverse('workbench:manageprojects'))


# Handles modification of projects
def handle_project_modification(mod_form):

    # Shorten calls
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

    return HttpResponseSeeOther(reverse('workbench:manageprojects'))


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
