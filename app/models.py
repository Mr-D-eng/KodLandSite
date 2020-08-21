from django.db import models
from datetime import date

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='blog')
    description = models.TextField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
