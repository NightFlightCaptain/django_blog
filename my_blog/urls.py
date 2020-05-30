# -*- coding:utf-8 -*-
# @Time      :2020/5/28 20:19
# @Author    :小栗旬
from django.urls import path

from my_blog import views

urlpatterns = [
    path('hello/', views.hello),

    path('',views.index,name='index')
]
