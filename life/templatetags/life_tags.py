# -*- coding: utf-8 -*-

from ..models import LPost
from django import template

register = template.Library()

@register.simple_tag()
def get_recent_post(num=3):
    """
    自定义目模板
    :param num: 表示显示文章的数目
    :return: 按创建时间查找最新的文章
    """
    return LPost.objects.all().order_by('-created_time')[:num]

@register.simple_tag()
def archives():
    """
    归档
    将博客按照时间来整理，相同时间段的博客放在一起
    :return:
    """
    return LPost.objects.dates('created_time', 'month', order='DESC')