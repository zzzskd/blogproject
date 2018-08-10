import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from comments.forms import CommentForm
from .models import Article, Category
# Create your views here.
def index(request):
    """　主页　"""
    article_list = Article.objects.all()[:10] # .order_by('-created_time')[:10]
    context = {'article_list': article_list}
    return render(request, 'blog/index.html', context)

def articles(request):
    """ 返回全部文章 """
    raise Http404
    
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.body = markdown.markdown(article.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    
    form = CommentForm()
    comment_list = article.comment_set.all()
    
    context = {'article': article, 'form': form, 'comment_list': comment_list}
    return render(request, 'blog/article_detail.html', context)

def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                            created_time__month=month
                                        ) # .order_by('-created_time')
    context = {'article_list': article_list}
    return render(request, 'blog/index.html', context)
    

def category(request, category_pk):
    cate = get_object_or_404(Category, pk=category_pk)
    article_list = Article.objects.filter(category=cate) # .order_by('-created_time')
    context = {'article_list': article_list}
    return render(request, 'blog/index.html', context)

