# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 生活博客的主要内容
class LPost(models.Model):
    # 博客的标题
    title = models.CharField('标题', max_length=70)
    # 博客的内容
    body = models.TextField('内容')
    # 博客的创建时间和修改时间
    created_time = models.DateTimeField('创建日期')
    modified_time = models.DateTimeField('修改日期')
    # 博客的配图
    img = models.ImageField('配图', upload_to='LImg')
    # 博客的作者
    author = models.ForeignKey(User, verbose_name='作者')

    def get_absolute_url(self):
        """
        反向解析函数，
        正向解析：根据用户输入的地址，匹配对应的url,然后返回给用户
        反向解析：根据url，生成相应的地址

        :return: Study是app_name(视图函数命名空间，在views.py中)，detail是url的命名空间
                 第二个参数是博客的id(pk),可以根据用户点击的不同而变化
        """
        return reverse('life:detail', kwargs={'pk': self.pk})

    # 内部类，用来将后台首页中的英文转化为中文
    class Meta:
        verbose_name = '慢生活'
        verbose_name_plural = '慢生活'
