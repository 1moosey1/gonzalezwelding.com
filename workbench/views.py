from django.shortcuts import render
from django.views.generic.edit import FormView

from workbench.forms import ProjectForm
from workbench.models import Project, Image


# Render workbench home
def workbench(request):
    return render(request, 'workbench/home.html')


# Create new project view
class NewProjectView(FormView):

    form_class = ProjectForm
    template_name = 'workbench/newproject.html'
    success_url = '/workbench/project/new/'

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
                uploaded_image = Image(image=file, project=new_project)
                uploaded_image.save()

                # Attach image to project
                new_project.images.add(uploaded_image)

            return self.form_valid(form)

        else:
            return self.form_invalid(form)


def manage_projects(request):
    return render(request, 'workbench/manageprojects.html')
