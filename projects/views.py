from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from projects.forms import ProjectForm, ModifyForm
from projects.models import Project
from projects.utility import handle_project_creation, handle_project_modification, handle_project_deletion


# Create a project
def create_project(request):

    # Check if POST
    if request.POST:

        create_form = ProjectForm(request.POST, files=request.FILES)
        if create_form.is_valid():

            messages.success(request, "Project has been created")
            return handle_project_creation(create_form)

    # Must be GET
    else:
        create_form = ProjectForm()

    context = {'form': create_form}
    return render(request, 'projects/projectcreate.html', context)


# Render project manager
def manage_projects(request):

    context = {'projects': Project.objects.all()}
    return render(request, 'projects/projectmanager.html', context)


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

            messages.success(request, "Project changes have been saved")
            return handle_project_modification(mod_form)

    # Must be GET
    else:
        mod_form = ModifyForm(project)

    context = {'form': mod_form, 'project': project}
    return render(request, 'projects/projectmodify.html', context)


# Delete a project
def delete_project(request, project_id):

    # If bad project_id or no project_id is provided display 404 page
    try:
        project = Project.objects.get(id=project_id)

    except (ValueError, ObjectDoesNotExist):
        return render(request, 'workbench/404.html', {'404message': 'Project not found!'}, status=404)

    # If post then delete is confirmed
    if request.POST:

        messages.success(request, "Project has been deleted")
        return handle_project_deletion(project)

    context = {'project': project}
    return render(request, 'projects/projectdelete.html', context)
