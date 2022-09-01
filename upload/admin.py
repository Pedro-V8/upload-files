from django.contrib import admin
from .models import Document
# Register your models here.

@admin.register(Document)
class AdminDocuments(admin.ModelAdmin):
    fields = ['title' , 'uploadedFile' , 'dateTimeOfUpload']
    list_display = ['id' ,'title' , 'uploadedFile' , 'dateTimeOfUpload']


