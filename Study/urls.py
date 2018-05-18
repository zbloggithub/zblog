# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # 从上一级目录下导入views文件

app_name = 'Study'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'category/(?P<pk>[0-9]+)/$', views.category, name='category')
]