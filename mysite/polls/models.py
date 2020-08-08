from django.db import models
from django.utils import timezone 
# ! For Python3 you must import datetime from datetime
import datetime
# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  # ! The __str__() method display an object in the Django admin site and as the value inserted into a template when it displays an object
  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model): 
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text
