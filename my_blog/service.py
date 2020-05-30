# -*- coding:utf-8 -*-
# @Time      :2020/5/27 23:48
# @Author    :小栗旬
from django.db.models import Q

from my_blog.models import Tag, Article


def get_tag_by_id(id):
    tag = Tag.objects.filter(id=id, is_deleted=False).first()
    return tag


def get_all_tags():
    tags = Tag.objects.all()
    return tags


def get_tags_by_map(maps):
    tags = Tag.objects.filter(**maps)
    return tags


def add_tag(name, created_by):
    return Tag.objects.create(name=name, created_by=created_by)


def delete_tag(id):
    if Tag.objects.filter(id=id, is_deleted=False).count() > 0:
        Tag.objects.filter(id=id).update(is_deleted=True)
        return True
    else:
        return False


def update_tag(id, maps):
    rows = Tag.objects.filter(id=id).update(**maps)
    if rows > 0:
        return True
    else:
        return False


def get_all_articles():
    articles = Article.objects.filter(is_deleted=False)
    return articles


def get_articles_by_maps(maps):
    articles = Article.objects.filter(**maps)
    return articles


def get_article_by_id(id):
    article = Article.objects.filter(id=id).first()
    return article
