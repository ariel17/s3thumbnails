#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Customs file storage to read media from MEDIA_URL instead of
Amazon S3.

Source: http://stackoverflow.com/questions/8688815/django-compressor-how-to-write-to-s3-read-from-cloudfront
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import urlparse

from django.conf import settings

from storages.backends.s3boto import S3BotoStorage


def domain(url):
    return urlparse.urlparse(url).hostname


class MediaFilesStorage(S3BotoStorage):
    """
    Reading media files from MEDIA_URL instead of Amazon S3.
    """
    def __init__(self, *args, **kwargs):
        # kwargs['bucket'] = settings.MEDIA_FILES_BUCKET
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.MEDIA_URL)
        super(MediaFilesStorage, self).__init__(*args, **kwargs)


class StaticFilesStorage(S3BotoStorage):
    """
    Reading static files from STATIC_URL instead of Amazon S3.
    """
    def __init__(self, *args, **kwargs):
        # kwargs['bucket'] = settings.STATIC_FILES_BUCKET
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.STATIC_URL)
        super(StaticFilesStorage, self).__init__(*args, **kwargs)
