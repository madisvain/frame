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
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/nodes/$', 'frame.structure.views.nodes', name='nodes'),
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/elements/$', 'frame.structure.views.elements', name='elements'),
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/loads/$', 'frame.structure.views.loads', name='loads'),
    
    # Graphs and rendering
    url(r'^frame/(?P<uuid>[a-zA-Z0-9]{6})/plot/(?P<format>[-\w]+)/$', 'structure.views.svg', name='plot'),
)
