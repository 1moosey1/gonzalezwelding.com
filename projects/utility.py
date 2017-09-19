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
