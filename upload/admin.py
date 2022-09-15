from django.contrib import admin
from .models import Conta

# Register your models here.

@admin.register(Conta)
class AdminDocuments(admin.ModelAdmin):
    fields = [
        'title',
        'empresa',
        'status',
        'imagem',
        'data_emissao',
        'data_validade',
        'user_id',
        'created_at',
        'updated_at'
    ] #
    list_display = [
        'id',
        'title',
        'empresa',
        'status',
        'imagem',
        'data_emissao',
        'data_validade',
        'user_id',
        'created_at',
        'updated_at'
    ] 
