#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Image application URL configuration.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url


urlpatterns = patterns('images',
    url(r'^$', 'views.list', name='list'),
)
