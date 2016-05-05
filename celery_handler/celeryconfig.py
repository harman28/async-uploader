# from __future__ import absolute_import
# from django.conf import settings

CELERY_ROUTES = {
	'async_uploader.tasks.async_save' : {'queue': 'upload_queue'}
}

# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json', 'pickle']
CELERY_TIMEZONE = 'Asia/Kolkata'
