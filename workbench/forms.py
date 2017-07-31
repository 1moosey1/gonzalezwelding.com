from django import forms
from workbench.models import Project


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