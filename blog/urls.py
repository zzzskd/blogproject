from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # 主页
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article_detail'), # 如果是 article_pk 会报错
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<category_pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
