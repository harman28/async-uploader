# -*- coding: utf-8 -*-
from django.db import models
from storages.backends.s3boto import S3BotoStorage
from myproject.settings import AWS_BUCKETS
import ipdb

def upload_file_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'files/%s_%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

class MyS3BotoStorage(S3BotoStorage):
    @property
    def bucket(self):
        ipdb.set_trace()
        bucket_name = AWS_BUCKETS[self._filename[-4:]]
        return self._get_or_create_bucket(bucket_name)

    def _save(self, name, content):
        self._filename = name
        return super(MyS3BotoStorage, self)._save(name, content)

class Document(models.Model):
    docfile = models.FileField(upload_to=upload_file_to,storage=MyS3BotoStorage())
