# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import SPost, SCategory
import markdown
from comments.forms import SCommentForm


# 因为在settings.py文件下面修改了'DIRS':  [os.path.join(BASE_DIR, 'templates')],
# 所以django会直接进入templates文件夹下寻找文件
# Blog/study.html是templates下的具体目录
def index(request):
    """
    render 函数会根据我们传入的参数来构造 HttpResponse

    all() 方法从数据库里获取了全部的文章，存在了 post_list 变量里。
    all 方法返回的是一个 QuerySet（可以理解成一个类似于列表的数据结构），

    由于通常来说博客文章列表是按文章发表时间倒序排列的，即最新的文章排在最前面，
    所以我们紧接着调用了 order_by 方法对这个返回的 queryset 进行排序。
    排序依据的字段是 created_time，即文章的创建时间。- 号表示逆序，如果不加 - 则是正序。
    """
    post_list = SPost.objects.all().order_by('-created_time')
    return render(request, 'Blog/study.html', context={
                      'post_list': post_list,
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
    form = SCommentForm()
    comment_list = post.scomments_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'Blog/detailPage.html', context=context)

def category(request, pk):
    """
    当用户点击分类中的某个分类时，页面会跳转到学无止境页面，并且在学无止境页面上显示所有该分类的博客文章
    :param request:
    :param pk:
    :return: 获取某个分类的所有文章，返回到study.html页面
    """
    cate = get_object_or_404(SCategory, pk=pk)
    post_list = SPost.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'Blog/study.html', context={'post_list':post_list})