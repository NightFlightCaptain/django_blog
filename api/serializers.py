# -*- coding:utf-8 -*-
# @Time      :2020/5/28 13:42
# @Author    :小栗旬

from rest_framework import serializers

from my_blog import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = models.Article
        fields = '__all__'
