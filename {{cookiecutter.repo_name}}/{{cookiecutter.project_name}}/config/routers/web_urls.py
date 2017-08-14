from django.conf.urls import url, include

urlpatterns = [
    url(r'^auth/', include('{{cookiecutter.project_name}}.apps.authentications.urls', namespace='auth')),
]