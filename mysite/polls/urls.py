# design URLs for an app
# django.conf.urls contains utility functions
from django.conf.urls import url
#  in the current directory (polls) import views
from . import views

# Here we are adding the views to the polls url i.e polls/<view> 
urlpatterns = [
  # TODOurl(regex, view, kwargs=None, name=None) 
  # The 'r' in front of each regular expression string tells Python that a string is “raw” – that nothing in the string should be escaped
  # !There’s no need to add a leading slash, because every URL has that.
  # !Adding the nameSpace to the urlCONF allows Django to know which app view to create for a url when using the {% url %} template tag
  # ex: /polls/
  url(r'^$', views.index, name='index'),
  # ex: /polls/<question_id>/
  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
  # ex: /polls/<question_id>/results
  url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
  # ex:
  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]