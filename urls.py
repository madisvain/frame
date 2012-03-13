#coding: utf-8

from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Main template
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),
    url(r'^new/$', 'frame.structure.views.new_frame', name='new_frame'),
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/$', 'frame.structure.views.frame', name='frame'),
    
    # Interface
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/members/$', 'frame.structure.views.members', name='members'),
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/loads/$', direct_to_template, {'template': 'loads.html'}, name='loads'),
    
    # Graphs and rendering
    url(r'^svg/$', 'structure.views.svg', name='svg'),
)
