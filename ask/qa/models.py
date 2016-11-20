from django.db import models
from django.db import connection
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new():
        return Question.objects.order_by('added_at')[:5]
    def popular():
        return Question.objects.order_by('rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default="", max_length=255)
    text = models.TextField(default="")
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)