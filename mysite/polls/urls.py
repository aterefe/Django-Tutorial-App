# django.conf.urls contains utility functions
from django.conf.urls import url
#  ?in current (polls) directory import views
from . import views

urlpatterns = [
  # ! url(regex, view, kwargs=None, name=None) 
  # Strings typically use raw string syntax (r'') so that they can contain sequences like \d without the need to escape the backslash with another backslash.
  url(r'^$', views.index, name='index')
]