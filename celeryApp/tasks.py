from celery import shared_task  
from celeryApp.models import GenerateFileLog
from django.http import HttpResponse  
import csv  
from django.core.files import File
from django.conf import settings
import time


@shared_task(bind=True)
def createcsv(self,FileName,numberofrow):
    # writer = csv.writer(open(settings.MEDIA_ROOT+"file"+f"{numberofrow}"+".csv", "w"))
    filename = f"{FileName}.csv"
    writer = csv.writer(open(settings.MEDIA_ROOT+""+filename, "w"))
    for i in range(numberofrow):
        writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    filename = filename
    dataCount = numberofrow
    data = GenerateFileLog.objects.create(filename=filename,dataCount=dataCount)
    data.save()
    return f"{filename} rows created"