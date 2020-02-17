
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ArticleCreateForm, ArticleEditForm
from .models import Article
from .filters import slugify


# Create your views here.


def home_view(request):
    head_title = "Blog"
    main_head = "Blog"
    article = Article.objects.order_by('num_views').last()
    context = {
        "main_head": main_head,
        "head_title": head_title,
        'article': article,
    }
    return render(request, 'home.html', context)

#CRUD (with list as part of retieve)
#Create
@staff_member_required
def article_create_view(request):
    form = ArticleCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = slugify(form.cleaned_data['title'])
        obj.author = request.user
        obj.save()
        form = ArticleCreateForm()

    head_title = "Create Article"
    main_head = "Create Article"

    context = {
        'form': form,
        "head_title": head_title,
        "main_head": main_head,
    }
    return render(request, 'article_create.html', context)


#Retrieve
def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.num_views += 1
    article.save()
    head_title = article.title
    main_head = "Selected Article:"
    context = {
        "article": article,
        "head_title": head_title,
        "main_head": main_head,
    }
    return render(request, 'article_detail.html', context)


#List
def articles_view(request):
    queryset = Article.objects.all() if request.user.is_staff else Article.objects.published()
    head_title = "Articles"
    main_head = "Articles"
    context = {
        "object_list": queryset,
        "head_title": head_title,
        "main_head": main_head,
    }
    return render(request, 'articles.html', context)


#Update
@staff_member_required
def article_edit_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if not request.user.is_superuser and request.user != article.author:
        raise Http404
    form = ArticleEditForm(request.POST or None, instance=article)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return redirect(f"/articles/{obj.slug}")
    head_title = "Edit Article"
    main_head = "Edit Article"
    context = {
        "article": article,
        "head_title": head_title,
        "main_head": main_head,
        "form": form,
    }
    return render(request, 'article_edit.html', context)


#Delete
@staff_member_required
def article_delete_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if not request.user.is_superuser and request.user != article.author:
        raise Http404
    if request.method == "POST":
        article.delete()
        return redirect("/articles")
    head_title = "Delete Article"
    main_head = "Delete Article"
    context = {
        "article": article,
        "head_title": head_title,
        "main_head": main_head,
    }
    return render(request, 'article_delete.html', context)
