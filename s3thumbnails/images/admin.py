#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration registration for 'Images' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_image')

    def link_image(self, obj):
        return u"<a href='{0}'>{0}</a>".format(obj.image.url)

    link_image.allow_tags = True
    link_image.short_description = u'Image'


admin.site.register(Image, ImageAdmin)
