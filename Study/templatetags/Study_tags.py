# -*- coding: utf-8 -*-
from ..models import SPost, SCategory
from django import template

# 实例化了一个 template.Library 类
register = template.Library()

# 将函数 get_recent_posts 装饰为 register.simple_tag
# 就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了
@register.simple_tag()
def get_recent_post(num=3):
    """
    自定义目模板
    :param num: 表示显示文章的数目
    :return: 按创建时间查找最新的文章
    """
    return SPost.objects.all().order_by('-created_time')[:num]

@register.simple_tag()
def get_categories():
    """
    自定义获取学习博客所有分类的模板
    :return: 查询到的博客的分类
    """
    return SCategory.objects.all()