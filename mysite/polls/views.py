# django.http is module that takes an http
# Each you write is responsible for instanting populating, and returning an HttpResponse
from django.http import HttpResponse

# Create your views here.

# The index page displays the latest few questions
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

# The detail page displays a question text, with no results but with a form to vote.
def detail (request, question_id):
  return HttpResponse("You're looking at question %s." %question_id)

# The results page displays results for a particular question.
def results(request, question_id):
  response = "You're looking at the results of question %s"
  return HttpResponse(response % question_id)

# The vote action handles voting for a particular choice in a particular question.
def vote (request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
