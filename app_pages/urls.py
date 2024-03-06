from django.urls import path
from .views import django, python, java, go, cpp, bosh_sahiyfa
urlpatterns = [
path('', bosh_sahiyfa, name="bosh_sahiyfa"),
path('django', django, name="django"),

path('python', python, name='python'),
path('java', java, name='java'),
path('cpp', cpp, name='cpp'),
path('go', go, name='go')


]