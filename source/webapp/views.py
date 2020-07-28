from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        text_full = request.POST.get('text_full')
        author = request.POST.get('author')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')
        article = Article.objects.create(title=title, text=text, text_full=text_full, author=author, status=status, created_at=created_at,)

        return redirect('article_view', pk=article.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

