from django import forms


class ContactForm(forms.Form):

    _css = {'class': 'form-control'}
    _text_input = forms.TextInput(attrs=_css)
    _text_area = forms.Textarea(attrs=_css)

    name = forms.CharField(widget=_text_input, max_length=36)
    email = forms.CharField(widget=_text_input, required=False)
    subject = forms.CharField(widget=_text_input, max_length=100)
    message = forms.CharField(widget=_text_area)

    def clean_message(self):

        message = self.cleaned_data['message']
        message_len = len(message)
        if message_len < 5:
            raise forms.ValidationError("Message must be at least 5 characters")

        return message
