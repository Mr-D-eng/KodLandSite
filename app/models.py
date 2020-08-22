from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    img = models.ImageField('Картинка', upload_to='img')
    description = models.CharField('Краткое описание', max_length=1000)
    text = models.TextField('Текст статьи', null=True)
    date = models.DateTimeField('Дата и время публикации', null=True, blank=True)

    def __str__(self):
        return self.title
