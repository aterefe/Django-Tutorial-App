# django.http is module that takes an http
# Each you write is responsible for instanting populating, and returning an HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request)
  return HttpResponse("Hello, world. You're at the polls index.")
