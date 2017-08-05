from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from workbench.utility import handle_project_creation, handle_project_modification
from workbench.forms import ProjectForm, ModifyForm
from workbench.models import Project


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
    return render(request, 'workbench/createproject.html', context)


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
        return render(request, 'workbench/404.html', {'404message': 'Project not found!'}, status=404)

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
    return render(request, 'workbench/deleteproject.html')
