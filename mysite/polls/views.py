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

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

# The vote action handles voting for a particular choice in a particular question.
def vote (request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    # request.POST is a dictionary-like object that lets you access submitted data by key name. request.POST values are always strings
    # !request.POST['choice'] returns the ID of the selected choice
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question Voting form.
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice."
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing with POST data. 
    # This prevents data from being posted twice if a user hits the Back button.
    return HttpResponseRedirect(reverse('results', args=(question.id,)))