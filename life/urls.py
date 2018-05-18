# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # 从上一级目录下导入views文件

app_name = 'life'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'lpost/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
]