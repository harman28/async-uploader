from __future__ import absolute_import
from django.shortcuts import get_object_or_404
from django.core.files.uploadedfile import InMemoryUploadedFile
from celery_handler.celery import app
import StringIO
@app.task
def async_save(data, file_info, typer, instance):
    print "Task Running"
    #doc is the data of the document read into a StringIO buffer
    doc = StringIO.StringIO(data['data'])
    #pass the StringIo, and a list of required args to InMemoryUploadedFile
    document = InMemoryUploadedFile(doc, *file_info)
    #add the name of the formfield to the instance's __dict__, and set the document to it. 
    instance.__dict__[file_info[0]] = document
    instance.save()