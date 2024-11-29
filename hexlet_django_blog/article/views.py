from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from hexlet_django_blog.article.form import ArticleForm
from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, "articles/index.html", context={"articles": articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/show.html", context={"article": article})


class ArticleCommentsView(View):
    def get(self, request, *args, **kwargs):
        comment = "Здесь будут комментарии"
        return render(request, "articles/comments.html", context={"comment": comment})


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", context={"form": form})

    def post(self, requst, *args, **kwargs):
        form = ArticleForm(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(requst, 'articles/create.html', context={"form": form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/edit.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'articles/edit.html', {'form': form, 'article_id': article_id})
    

class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('index')
