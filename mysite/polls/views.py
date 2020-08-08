# django.http is module that takes an http
# Each you write is responsible for instanting populating, and returning an HttpResponse or render
# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Choice, Question
# Create your views here.

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'
  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.order_by('-pub_date')[:5]