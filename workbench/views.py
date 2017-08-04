from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from workbench.forms import ProjectForm, ModifyForm
from workbench.models import Project, Image


# Render workbench home
def workbench(request):
    return render(request, 'workbench/home.html')


# Create a project
def create_project(request):

    # Check if POST
    if request.POST:

        create_form = ProjectForm(request.POST, files=request.FILES)
        if create_form.is_valid():
            return handle_project_creation(create_form)

    # Must be GET
    else:
        create_form = ProjectForm()

    context = {'form': create_form}
    return render(request, 'workbench/newproject.html', context)


# Render project manager
def manage_projects(request):

    context = {'projects': Project.objects.all()}
    return render(request, 'workbench/manageprojects.html', context)


# Modify a project
def modify_project(request, project_id):

    # If bad project_id or no project_id is provided display 404 page
    try:
        project = Project.objects.get(id=project_id)

    except (ValueError, ObjectDoesNotExist):
        return render(request, 'workbench/404.html', {'404message': 'Project not found!'})

    # Check if POST
    if request.POST:

        mod_form = ModifyForm(project, request.POST, files=request.FILES)
        if mod_form.is_valid():
            return handle_project_modification(mod_form)

    # Must be GET
    else:
        mod_form = ModifyForm(project)

    context = {'form': mod_form, 'project': project}
    return render(request, 'workbench/modifyproject.html', context)


# Delete a project
def delete_project(request, project_id):
    pass


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

    return redirect(reverse('workbench:manageprojects'))


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

    return redirect(reverse('workbench:manageprojects'))


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
