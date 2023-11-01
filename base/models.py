from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __abs__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', args=str(self.id))