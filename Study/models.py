# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 学习博客中博客分类，将博客分为不同的类型，以便更好地寻找博客
class SCategory( models.Model):
    """
    max_length表示数据库中最大能存取的字符
    """
    name = models.CharField('分类', max_length=100)

    # 解决的问题：
    # Django的model中使用了外键，在页面显示时，显示不出已有的内容，而是Category_object
    # 用于返回对象的属性
    def __unicode__(self):
        return self.name

    # 内部类，用来将后台首页中的英文转化为中文
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

# 学习博客的标签
class STag(models.Model):
    name = models.CharField('标签', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

# 博客的主要内容
class SPost(models.Model):
    # 博客标题
    title = models.CharField('标题', max_length=70)

    # 博客正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField('内容')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField('创建日期')
    modified_time = models.DateTimeField('修改日期')

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField('简介', max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。

    category = models.ForeignKey(SCategory, verbose_name='分类')
    tags = models.ManyToManyField(STag, blank=True, verbose_name='标签')
    # upload_to表示图片存放的文件夹
    img = models.ImageField('配图', upload_to='SImg')

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User, verbose_name='作者')

    # 博客的图片，每一篇博客都会配不同的图片
    # class SPicture(models.Model):
    #     """
    #     upload_to表示图片存放的文件夹
    #     """
    #     img = models.ImageField(upload_to='SImg')
    #     post = models.ForeignKey(SPost)

    def get_absolute_url(self):
        """
        反向解析函数，
        正向解析：根据用户输入的地址，匹配对应的url,然后返回给用户
        反向解析：根据url，生成相应的地址

        :return: Study是app_name(视图函数命名空间，在views.py中)，detail是url的命名空间
                 第二个参数是博客的id(pk),可以根据用户点击的不同而变化
        """
        return reverse('Study:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = '学无止境'
        verbose_name_plural = '学无止境'

