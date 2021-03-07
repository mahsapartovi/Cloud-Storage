from django import forms
from . import models

class UserFile(forms.Form):
    file = forms.FileField(required=True)
