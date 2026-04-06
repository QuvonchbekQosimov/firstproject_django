from django.shortcuts import render
from .tests import datas, Capital
from .models import Article
def home(request):
    capitals = [Capital(d[0], d[1], d[2], d[3], d[4]) for d in datas]
    return render(request, 'home.html',
                  context={
                      'capitals': capitals,
                      'title':'Poytaxtlar Haqida',
                      'yakun':'Tamom !'
                  })

def page(request):
    return render(request, 'page.html')


def news(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'sarlavha':'Jahon yangiliklari'
    }
    return render(request, 'news.html', context=context)
def new_detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }
    return render(request, 'new_detail.html', context=context)
