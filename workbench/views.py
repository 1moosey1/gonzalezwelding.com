from django.shortcuts import render
from django.views.generic.edit import FormView

from workbench.forms import ProjectForm
from workbench.models import Project


# Render workbench home
def workbench(request):
    return render(request, 'workbench/home.html')


# Create new project view
class NewProjectView(FormView):

    form_class = ProjectForm
    template_name = 'workbench/newproject.html'
    success_url = '/gwm/newproject/'

    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        files = request.FILES.getlist('imagefield')

        if form.is_valid():
            for f in files:
                fs.save(f.name, f)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
