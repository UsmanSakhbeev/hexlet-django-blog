from django.http import HttpResponse
from django.views import View


class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {"app_name": "Articles"}
        return HttpResponse(context)


"""
def index(request):
    # Передаем название приложения через контекст
    context = {"app_name": "Articles"}
    return render(request, "articles/index.html", context)
"""
