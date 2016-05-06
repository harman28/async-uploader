from __future__ import absolute_import

from django.shortcuts import get_object_or_404
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.cache import cache

from storages.backends.s3boto import S3BotoStorage

from celery_handler.celery import app

import StringIO
import os

@app.task
def async_save(data, file_info, typer, instance):
    print "Task Running"
    #doc is the data of the document read into a StringIO buffer
    doc = StringIO.StringIO(data['data'])
    #pass the StringIo, and a list of required args to InMemoryUploadedFile
    document = InMemoryUploadedFile(doc, *file_info)
    #add the name of the formfield to the instance's __dict__, and set the document to it. 
    instance.docfile = document
    # filename_base, filename_ext = os.path.splitext(document.name)
    # instance.docfile.storage = S3BotoStorage(bucket="asynch-uploader-%s"%(filename_ext[1:]))
    instance.save()
    cache.clear()