from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<article_pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<category_pk>[0-9]+)/$', views.category, name='category'),
]
