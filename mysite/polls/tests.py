import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# TODO: Created a django.test.TestCase subclass with a method that creates a Question instance with a pub_date in the future
class QuestionModelTest(TestCase):
  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() returns False for question whose pub_date is in the future
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)
