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

class Transacao(models.Model):
    banco_origem = models.CharField(max_length=200)
    agencia_origem = models.CharField(max_length=200)
    conta_origem = models.CharField(max_length=200)
    banco_destino = models.CharField(max_length=200)
    agencia_destino = models.CharField(max_length=200)
    conta_destino = models.CharField(max_length=200)
    valor_transacao = models.IntegerField()
    data_hora = models.CharField(max_length=200)
    upload_id = models.ForeignKey(Document , on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name = 'Transacao'
        verbose_name_plural = 'Transacoes'
