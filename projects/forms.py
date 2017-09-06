from django import forms
from projects.models import Project


class ProjectForm(forms.Form):

    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea, max_length=512, required=False)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def clean_title(self):

        title = self.cleaned_data['title']
        project = Project.objects.filter(title=title)

        if len(project) > 0:
            raise forms.ValidationError('Duplicate project title! Please choose a unique project title.')

        return title


class ModifyForm(ProjectForm):

    def __init__(self, project, *args, **kwargs):

        super(ModifyForm, self).__init__(*args, **kwargs)
        self.project = project

        # Set initial values for title/description and modify images requirement
        self.fields['title'].initial = project.title
        self.fields['description'].initial = project.description
        self.fields['images'].required = False

        # Create checkboxes for every image in the project
        self.create_checkboxes()

    def create_checkboxes(self):

        images = self.project.images.all()
        choices = []

        for i in range(len(images)):
            choices.append((images[i].id, ''))

        self.fields['checkboxes'] = \
            forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices)
        self.fields['checkboxes'].required = False

    def clean_title(self):

        title = self.cleaned_data['title']
        project = Project.objects.filter(title=title)

        # Only raise validation error if the project conflicts with other names and not its own
        if len(project) and project[0].title != self.project.title:
            raise forms.ValidationError('Duplicate project title! Please choose a unique project title.')

        return title
