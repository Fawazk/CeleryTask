from django.db import models

class GenerateFileLog(models.Model):
    filename = models.CharField(max_length=200)
    dataCount = models.IntegerField()

    # 

