from django.shortcuts import render
from django.views.generic.edit import FormView

from workbench.forms import ProjectForm
from workbench.models import Project, Image


# Render workbench home
def workbench(request):
    return render(request, 'workbench/home.html')


# Create a new project view
class NewProjectView(FormView):

    form_class = ProjectForm
    template_name = 'workbench/newproject.html'
    success_url = '/workbench/project/manage/'

    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        # Get all uploaded images
        files = request.FILES.getlist('images')

        if form.is_valid():

            # Create new project and save it
            new_project = Project(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
            new_project.save()

            for file in files:

                # Create new image based on uploaded image and save it
                uploaded_image = Image(image_field=file, project=new_project)
                uploaded_image.save()

                # Attach image to project
                new_project.images.add(uploaded_image)

            return self.form_valid(form)

        else:
            return self.form_invalid(form)


# Project Manager
def manage_projects(request):

    context = {'projects': Project.objects.all()}
    return render(request, 'workbench/manageprojects.html', context)


from django.http import HttpResponse
# Modify or delete a project
def modify_project(request, project_name):
    return HttpResponse("Modify: " + project_name)
