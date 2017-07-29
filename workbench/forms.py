from django import forms


class ProjectForm(forms.Form):

    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea, max_length=512)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
