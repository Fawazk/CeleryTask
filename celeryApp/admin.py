from django.contrib import admin
from .models import GenerateFileLog

# Register your models here.
class GenerateClass(admin.ModelAdmin):
    list_display = ('filename','dataCount')

admin.site.register(GenerateFileLog,GenerateClass)