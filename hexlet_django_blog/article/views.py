from django.shortcuts import HttpResponse, redirect
from django.urls import reverse


def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {tags}. Тег {article_id}")


def home(request):
    url = reverse("article", kwargs={"tags": "python", "article_id": 42})
    return redirect(url)
    