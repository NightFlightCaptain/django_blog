# -*- coding:utf-8 -*-
# @Time      :2020/5/27 23:48
# @Author    :小栗旬

from django import forms

from my_blog import models


class AddTagForm(forms.Form):
    name = forms.CharField(max_length=30, required=True,
                           error_messages={
                               "max_length": "用户名不能超过30",
                               "required": "用户名不存在"
                           })
    created_by = forms.CharField(max_length=255,required=True)

