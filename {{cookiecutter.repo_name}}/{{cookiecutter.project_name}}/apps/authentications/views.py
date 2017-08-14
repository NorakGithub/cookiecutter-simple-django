from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from {{cookiecutter.project_name}}.apps.authentications.forms import LoginForm

class LoginView(FormView):
    template_name = 'authentications/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('auth:success')

    def form_valid(self, form):
        form.login(request=self.request)
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('auth:login'))


# TODO This success view is meant only for sample, you should remove it
class SuccessView(TemplateView):
    template_name = 'authentications/success.html'
