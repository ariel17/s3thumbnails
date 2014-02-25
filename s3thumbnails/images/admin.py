#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration registration for 'Images' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_image', 'link_thumbnail')

    def link_image(self, obj):
        return u"<a href='{0}'>{0}</a>".format(obj.image.url)

    link_image.allow_tags = True
    link_image.short_description = u'Image'

    def link_thumbnail(self, obj):
        return u"<a href='{0}'>{0}</a>".format(obj.thumbnail().url)

    link_thumbnail.allow_tags = True
    link_thumbnail.short_description = u'Thumbnail'


admin.site.register(Image, ImageAdmin)
