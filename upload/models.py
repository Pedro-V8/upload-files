from tabnanny import verbose
from django.db import models
from django.utils import timezone
# Create your models here.

def upload_document(instance , filename):
    return f"{instance.id}-{filename}"

class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to=upload_document)
    dateTimeOfUpload = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name = 'Document'
        verbose_name_plural = 'Documentos'
