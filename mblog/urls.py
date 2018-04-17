"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainsite import views
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index),
    url('^list/$',views.listing),
    url('^list/(\d+)/$',views.disp_detail),#list/002,默认传参
    # url('^list/(?P<sku>\d+)$',views.disp_detail) #自动传参
    # url(r'^list/$',views.disp_detail,{'test':'yes'}),#手动传参
    url(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,3})',views.post), #传递多个参数
    url('^about/$',views.about),

    url(r'^video/(\d+)/$',views.video,name='tv-url'),#视频页面

    url(r'',views.index), #如果输入错误地址，返回主页

]
