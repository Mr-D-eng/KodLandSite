from django.shortcuts import render
from .models import Article
from django.http import Http404

# Create your views here.
def main(request):
    info=Article.objects.all()
    latest_articles=Article.objects.order_by('-date')[:1]

    return render(request, 'html/main.html', context={'info':info, 'latest_articles':latest_articles})

def add(request):
    return render(request, 'html/add.html')

def detail(request, article_id):
    try:
        a= Article.objects.get( id = article_id)
    except:
        raise http404("Статья не найдена")

    return render(request, 'html/article.html', context={'article':a})
