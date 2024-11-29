from django.urls import path

from .views import (
    ArticleCommentsView,
    ArticleFormCreateView,
    ArticleFormDeleteView,
    ArticleFormEditView,
    ArticleView,
    IndexView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/", ArticleView.as_view(), name="article"),
    path(
        "<int:article_id>/comments/<int:id>/",
        ArticleCommentsView.as_view(),
        name="comment",
    ),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="articles_delete"),
]
