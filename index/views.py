# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from Study.models import SPost
from life.models import LPost
import markdown

def index(request):
    SPost_list = SPost.objects.all().order_by('-created_time')
    LPost_list = LPost.objects.all().order_by('-created_time')
    return render(request, 'Index/index.html', context={
        'SPost_list': SPost_list, 'LPost_list': LPost_list,
    })

def detail(request, pk):
    """
    当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，
    如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    markdown是根据特定的格式来输出文本
    :param request:
    :param pk: 博客的id
    :return: 获取博客所有的内容，并且跳转到detail.html页面去
    """
    post = get_object_or_404(SPost, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'Index/detailPage.html', context={'post': post})