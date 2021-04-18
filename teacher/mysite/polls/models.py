import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Paper(models.Model):
    author = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='')
    citation = models.IntegerField(default=0)
    pub_date = models.IntegerField(default=2000)
    filename = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title
class Comment(models.Model):
    teacher = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.content
class Login(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username