# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # 从上一级目录下导入views文件

app_name = 'Index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'Ipost/(?P<pk>[0-9]+)/$', views.detail, name='detail')
]