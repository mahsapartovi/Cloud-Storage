from django import forms


class Login(forms.Form):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())




