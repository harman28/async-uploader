# -*- coding: utf-8 -*-
from django.db import models
from storages.backends.s3boto import S3BotoStorage

def upload_file_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'files/%s_%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

def aws_bucket(instance, filename):
    import os
    filename_base, filename_ext = os.path.splitext(filename)
    return 'asynch-uploader-%s' %(filename_ext[1:])


class Document(models.Model):
    docfile = models.FileField(upload_to=upload_file_to)
