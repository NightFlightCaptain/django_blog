from enum import Enum

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from my_blog import service, models
from api import serializers


class Resp:
    def __init__(self):
        code = Code.success
        message = get_resp_message(code)
        data = None

    @staticmethod
    def success(code, data):
        resp = Resp()
        resp.code = code
        resp.message = get_resp_message(code)
        resp.data = data

        return resp


class Code(Enum):
    success = 200
    tag_not_fount = 401

    error = 500


def get_resp_message(code):
    messages = {
        Code.success: "成功",
        Code.tag_not_fount: "标签不存在",
        Code.error: "服务器错误"
    }
    return messages[code]


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    # return render(request, 'hello.html', context)
    return HttpResponse("welcome!")


def add_tag(name, created_by):
    tag = service.add_tag(name, created_by)
    serializer_class = serializers.TagSerializer
    queryset = Resp.success(Code.success, tag)


def index(request):
    article_id = request.GET.get('id')
    blog_index = models.Article.objects.filter(id=article_id)
    context = {'blog_index': blog_index}
    return render(request, 'index.html', context)
