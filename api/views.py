# -*- coding:utf-8 -*-
# @Time      :2020/5/28 16:35
# @Author    :小栗旬
from django.http import Http404
from django.views import View
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api import serializers
from api.serializers import TagSerializer
from my_blog import service
from my_blog.models import Tag, Article


class StandardResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ResultMsg:
    def __init__(self, code=200, msg='success', data=None):
        self.code = code
        self.msg = msg
        self.data = data

    def dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'data': self.data,
        }


class ResponseModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(ResultMsg(data=response.data).dict(), headers=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(ResultMsg(data=response.data).dict(), headers=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(ResultMsg(data=response.data).dict(), headers=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(ResultMsg(data=response.data).dict(), headers=response.status_code)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(ResultMsg(data=response.data).dict(), headers=response.status_code)


class TagListView(GenericAPIView):
    def get_serializer_class(self):
        return TagSerializer

    def get_queryset(self):
        return service.get_all_tags()

    def get(self, request):
        maps = {}
        params = request.query_params
        for k in params:
            maps[k] = params.get(k)
        tags = service.get_tags_by_map(maps)

        if len(tags) == 0:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        result = self.get_serializer(tags, many=True)
        return Response(result.data)

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

        instance = serializer.save()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)


class TagDetailView(RetrieveAPIView):

    def get_serializer_class(self):
        return TagSerializer

    def get_queryset(self):
        return service.get_all_tags()

    # def get(self, request, pk):
    #     return self.retrieve(request, pk)

    # def get(self, request, pk):
    #     serializer = self.get_serializer(instance=self.get_object())
    #     if serializer is None:
    #         return Response()
    #     return Response(serializer.data)

    def put(self, request, pk):
        if service.update_tag(pk, maps=request.data):
            return Response(True)
        return Response(False, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if service.delete_tag(pk):
            return Response(True)
        return Response(False, status=status.HTTP_400_BAD_REQUEST)


#
# class ArticleList(ListCreateAPIView):
#     serializer_class = serializers.ArticleSerializer
#     queryset = service.get_all_articles()

#
# class ArticleView(RetrieveUpdateDestroyAPIView):
#     queryset = service.get_all_articles()
#     serializer_class = serializers.ArticleSerializer
#


class ArticleDetailView(ModelViewSet):
    """
    list:
        查看所有文章
    create:
        新增一篇文章
    retrieve:
        获取一篇文章
    destroy:
        删除一篇文章
    update:
        修改一篇文章
    """
    queryset = service.get_all_articles()
    serializer_class = serializers.ArticleSerializer
    pagination_class = StandardResultSetPagination

    @action(methods=['get'], detail=False)
    def count(self, request):
        articles = self.get_queryset()
        count = len(articles)
        return Response(ResultMsg(data=count).dict())

    @action(methods=['get'], detail=False, url_path='names')
    def get_names(self, request) -> Response:
        """
        获取名称中包含给定字符的文章名

        """
        title_filter = request.GET.get('title')
        if title_filter is None:
            title_filter = ''
        names = Article.objects.filter(title__contains=title_filter).values_list('title', 'desc')
        return Response(ResultMsg(data=names).dict())

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response(ResultMsg(code=400, msg='失败'))
        instance.is_deleted = True
        instance.save()
        return Response(ResultMsg().dict())
