from django.contrib import admin
from .models import Document , Transacao

# Register your models here.

@admin.register(Document)
class AdminDocuments(admin.ModelAdmin):
    fields = ['title' , 'uploadedFile' , 'dateTimeOfUpload']
    list_display = ['id' ,'title' , 'uploadedFile' , 'dateTimeOfUpload']

@admin.register(Transacao)
class AdminTransacao(admin.ModelAdmin):
    fields = [
        'banco_origem',
        'agencia_origem',
        'conta_origem',
        'banco_destino',
        'agencia_destino',
        'conta_destino' ,
        'valor_transacao',
        'data_hora',
        'upload_id',
        'created_at'
    ]
    list_display = [
        'id',
        'banco_origem',
        'agencia_origem',
        'conta_origem',
        'banco_destino',
        'agencia_destino',
        'conta_destino',
        'valor_transacao',
        'data_hora',
        'upload_id',
        'created_at'
    ]


