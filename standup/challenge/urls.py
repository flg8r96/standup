__author__ = 'flg8r96'
from django.conf.urls import patterns, url
#from django.views.generic import TemplateView
from challenge import views

print "in challenge urls.py"
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#    url(r'^$', views.test, natest'),
)

print "end challenge urls.py"
