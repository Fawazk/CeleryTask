from celery import shared_task  
from celeryApp.models import GenerateFileLog
from django.http import HttpResponse  
import csv  
from django.core.files import File
from django.conf import settings
import time


@shared_task(bind=True)
def createcsv(self,numberofrow):
    writer = csv.writer(open(settings.MEDIA_ROOT+"file"+f"{numberofrow}"+".csv", "w"))
    for i in range(numberofrow):
        writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    filename = 'file'
    dataCount = numberofrow
    data = GenerateFileLog.objects.create(filename=filename,dataCount=dataCount)
    data.save()
    return f"{numberofrow} rows created"