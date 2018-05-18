# -*- coding: utf-8 -*-

from django import forms
from .models import LComments, SComments

# 为了使用方便，给每个表单定义一个数据库模型，这样使用modelform类会更方便一点
# 通过调用这个两个类的一些方法和属性，Django 将自动为我们创建常规的表单代码，
class LCommentForm(forms.ModelForm):
    class Meta:
        model = LComments  # 用来指定表单对应的数据库类型
        fields = ['name', 'email', 'text']  # 用来指定表单需要显示的字段

class SCommentForm(forms.ModelForm):
    class Meta:
        model = SComments
        fields = ['name', 'email', 'text']