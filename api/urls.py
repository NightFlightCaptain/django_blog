# -*- coding:utf-8 -*-
# @Time      :2020/5/28 16:35
# @Author    :小栗旬
from django.urls import path, include
from rest_framework import reverse
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from api.views import TagListView, TagDetailView, ArticleDetailView

app_name = 'api'

router = DefaultRouter()
router.register('article', ArticleDetailView)

urlpatterns = [
    path(r'tags/', TagListView.as_view()),
    path(r'tag/<int:pk>', TagDetailView.as_view()),

    # 可以被router替换
    # path(r'articles/', ArticleView.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # })),
    # path(r'article/<int:pk>', ArticleView.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),

    path('', include(router.urls), name='article'),
    # path('article/count', ArticleDetailView.as_view({'get': 'count'})),

    path('docs/', include_docs_urls('接口文档')),
]
