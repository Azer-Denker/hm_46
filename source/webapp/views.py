from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Article.objects.all()
    else:
        data = Article.objects.filter(status='moderated')
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
        text_full = request.POST.get('text_2')
        author = request.POST.get('author')
        status = request.POST.get('status')
        article = Article.objects.create(title=title, text=text, text_full=text_full, author=author, status=status)

        return redirect('article_view', pk=article.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
