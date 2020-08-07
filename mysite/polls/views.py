# django.http is module that takes an http
# Each you write is responsible for instanting populating, and returning an HttpResponse or render
# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager.
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
# Create your views here.

# The index page displays the latest few questions
def index(request):
  # getting the top 5 latest question
  latest_quesstion_list = Question.objects.order_by('-pub_date')[:5]
  # context is a dictionary mapping template variable names to Python objects.
  context = {'latest_question_list' : latest_quesstion_list}
  # The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.
  return render(request, 'polls/index.html', context)

# The detail page displays a question text, with no results but with a form to vote.
def detail (request, question_id):
  question = get_object_or_404(Question, id=question_id) 
  return render(request, 'polls/detail.html', {'question': question})

# The results page displays results for a particular question.
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

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
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
