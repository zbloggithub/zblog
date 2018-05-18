# -*- coding: utf-8 -*-
"""ZBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

"""
当用户访问不同的网址时，应该如何处理这些不同的网址（即所说的路由）：
Django 的做法是把不同的网址对应的处理函数写在一个 urls.py 文件里，
当用户访问某个网址时，Django 就去会这个文件里找，如果找到这个网址，
就会调用和它绑定在一起的处理函数（叫做视图函数）。
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('index.urls')),
    url(r'^study/', include('Study.urls')),
    url(r'^life/', include('life.urls')),
    url(r'', include('comments.urls')),
]
