from django.contrib import admin
from django.conf.urls import url
from . import views

#url patterns 

urlpatterns = [
    url('',views.begin,name='begin'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^index', views.index, name='index'),
    url(r'^otp', views.otp, name='otp'),
]
