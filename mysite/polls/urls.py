# design URLs for an app
# django.conf.urls contains utility functions
from django.conf.urls import url
#  ?in current (polls) directory import views
from . import views

urlpatterns = [
  # TODOurl(regex, view, kwargs=None, name=None) 
  # The 'r' in front of each regular expression string tells Python that a string is “raw” – that nothing in the string should be escaped
  # !There’s no need to add a leading slash, because every URL has that.
  url(r'^$', views.index, name='index')
]