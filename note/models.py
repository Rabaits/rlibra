from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField("name note", max_length=200)
    brief = models.TextField("brief note")
    text = models.TextField("text note")
    data = models.DateTimeField("data note", auto_now_add=True) 