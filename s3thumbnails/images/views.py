#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: A dummy view that lists images and thumbnails URL. All stored on
             an S3 bucket.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render_to_response
from django.template import RequestContext

from images.models import Image


def list(request):
    """
    Lists the images URL and thumbnails from S3 bucket.
    """
    return render_to_response('images_list.html', {
        'images': Image.objects.all(),
    }, context_instance=RequestContext(request))
