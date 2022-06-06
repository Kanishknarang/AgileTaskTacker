from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[('Todo','Todo'), ('inProgress','inProgress'), ('inreview','inreview'), ('closed','closed')])
    priority = models.CharField(max_length=100, choices=[('low','low'), ('medium','medium'), ('high','high')])
    card_type = models.CharField(max_length=100, choices=[('feature','feature'),('issue','issue')], default = 'feature')
    date_created = models.DateTimeField(default=timezone.now)
    assignee = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})    
