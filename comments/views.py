# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from Study.models import SPost
from life.models import LPost

from .models import SComments, LComments
from .forms import SCommentForm, LCommentForm

def Spost_comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post = get_object_or_404(SPost, pk=post_pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = SCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)

        else:
            comment_list = post.scomments_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
        return render(request, 'Blog/detailPage.html', context=context)

    return redirect(post)

