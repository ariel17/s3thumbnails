#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: A dummy model to contain images.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models


class Image(models.Model):
    """
    A dummy model to contain images.
    """
    image = models.ImageField(upload_to=settings.IMAGES_UPLOAD_TO)

    def thumbnail(self):
        """
        Creates a thumbnail from the current image, just to put the thumbnail
        framework to work.
        """
        return None
