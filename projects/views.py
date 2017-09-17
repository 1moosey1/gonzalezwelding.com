from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from workbench.utility import NoContentRedirect, HttpResponseSeeOther, render404
from projects.forms import ProjectForm, ModifyForm
from projects.models import Project
from projects.utility import get_project, handle_project_creation, handle_project_modification, \
    handle_project_deletion, filter_projects, create_prange


# Render project manager
def manage_projects(request):

    # If no projects render page with no context
    projects = Project.objects.all()
    if not projects.exists():
        return render(request, 'projects/projectmanager.html')

    # Parse page number
    page = request.GET.get('page', 0)

    try:
        page = abs(int(page))

    except ValueError:
        page = 0

    context = {

        'projects': filter_projects(projects, page),
        'current_page': page,
        'page_range': create_prange(projects, page)
    }

    return render(request, 'projects/projectmanager.html', context)


# Create a project
def create_project(request):

    if request.POST:

        create_form = ProjectForm(request.POST, files=request.FILES)
        if create_form.is_valid():

            handle_project_creation(create_form)

            messages.success(request, "Project has been created")
            return HttpResponseSeeOther(reverse('projects:manager'))

    else:
        create_form = ProjectForm()

    # Return GET 200
    context = {'form': create_form}
    return render(request, 'projects/projectcreate.html', context)


# Modify a project
def modify_project(request, project_id):

    # Return 404 if project can not be found
    project = get_project(project_id)
    if not project:
        return render404(request, 'Project not found!')

    if request.POST:

        mod_form = ModifyForm(project, request.POST, files=request.FILES)
        if mod_form.is_valid():

            # Prevent multiple submissions
            if request.session.pop('modify', False):

                handle_project_modification(mod_form)
                messages.success(request, "Project changes have been saved")

            return HttpResponseSeeOther(reverse('projects:manager'))

    else:
        mod_form = ModifyForm(project)

    # Allow session to submit modify once
    request.session['modify'] = True

    # Return GET 200
    context = {'form': mod_form, 'project': project}
    return render(request, 'projects/projectmodify.html', context)


# Delete a project
def delete_project(request, project_id):

    # Return 404 if project can not be found
    project = get_project(project_id)
    if not project:
        return render404(request, 'Project not found!')

    # Handle delete request
    if request.method == "DELETE":

        handle_project_deletion(project)

        messages.success(request, "Project has been deleted")
        return NoContentRedirect(reverse('projects:manager'))

    # Return GET 200
    context = {'project': project}
    return render(request, 'projects/projectdelete.html', context)
