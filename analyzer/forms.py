from django import forms

class GraphUploadForm(forms.Form):
    image = forms.ImageField()
