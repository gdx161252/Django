from django.shortcuts import render
from django.http import  HttpResponse
from django.core import  serializers
from django.template.defaultfilters import title
from crud_blog_web.models import Article


# Create your views here.

def indexArticleJson(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


def index(request):
    return HttpResponse("Hello, world. You're at the ")

def indexArticle(request):
    title = "Lista artykółów"
    articles = Article.objects.all()
    return render(request, 'Article.html', {
        'title': title,
        'articles': articles,
    })