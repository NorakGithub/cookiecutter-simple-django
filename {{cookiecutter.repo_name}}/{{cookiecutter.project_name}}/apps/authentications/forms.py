from django import forms
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError(_("Invalid username or password"))

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
