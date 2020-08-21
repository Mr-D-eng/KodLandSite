from django.shortcuts import render
from .models import Article

# Create your views here.
def main(request):
    return render(request, 'html/main.html')

def add(request):
    return render(request, 'html/add.html')

def article(request):
    return render(request, 'html/article.html')
