from django.shortcuts import render
from .tests import datas, Capital
from .models import Article, Category


def news(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'sarlavha':'Jahon yangiliklari'
    }
    return render(request, 'news.html', context=context)


def by_category(request, id):
    articles = Article.objects.filter(category=id)
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'sarlavha':'Jahon yangiliklari'
    }
    return render(request, 'news.html', context=context)


def new_detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }
    return render(request, 'new_detail.html', context=context)
