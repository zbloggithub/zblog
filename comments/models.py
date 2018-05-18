# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

# 学无止境博客的评论
@python_2_unicode_compatible  # 这个装饰器用来兼容python2
class SComments(models.Model):
    name = models.CharField(max_length=100)  # 名称
    email = models.EmailField(max_length=255)  # 邮箱
    text = models.TextField()  # 评论内容
    created_time = models.DateField(auto_now_add=True)  # 自动生成评论时间

    post = models.ForeignKey('Study.SPost')  # 博客与评论是一对多的关系

    def __str__(self):
        return self.text[:20]

# 慢生活的评论
@python_2_unicode_compatible
class LComments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True)

    post = models.ForeignKey('life.LPost')

    def __str__(self):
        return self.text[:20]
