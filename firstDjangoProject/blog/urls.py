
from django.urls import path,re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

app_name='blog'
urlpatterns = [
    path('', views.index,name="index"),
    url(r'^p/(?P<id>[0-9]+)', views.show,name="show"),
    
]
