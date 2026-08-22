from django.shortcuts import get_object_or_404, render

from .models import Article, Publication


def publication_list(request):
    publications = Publication.objects.filter(is_published=True)
    return render(request, "insights/publication_list.html", {"publications": publications})


def publication_detail(request, slug):
    publication = get_object_or_404(Publication, slug=slug, is_published=True)
    return render(request, "insights/publication_detail.html", {"publication": publication})


def article_list(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, "insights/article_list.html", {"articles": articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, "insights/article_detail.html", {"article": article})
