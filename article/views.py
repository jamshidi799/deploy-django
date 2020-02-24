from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article_detail.html', {'article': article})


def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'new_article.html', {'form': form})