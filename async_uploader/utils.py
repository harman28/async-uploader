from .tasks import async_save


import ipdb
def save_document(documentfield_data, instance):
    #deconstruct the file into something celery can pickle and send to the worker
    data = {}
    file_info = []
    file_info.append(documentfield_data.field_name)
    file_info.append(documentfield_data.name)
    file_info.append(documentfield_data.content_type)
    file_info.append(documentfield_data.size)           
    file_info.append(documentfield_data.charset)
    #the actual data of the document, read into a string
    data['data'] = documentfield_data.read()
            
    #send the document to be saved by a worker
    # ipdb.set_trace()
    async_save.delay(data, file_info, instance.__class__, instance)