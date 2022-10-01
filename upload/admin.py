from django.contrib import admin
from .models import Conta , Responsaveis

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
        'valor',
        'user_id',
    ] #
    list_display = [
        'id',
        'title',
        'empresa',
        'status',
        'imagem',
        'data_emissao',
        'data_validade',
        'valor',
        'user_id',
        'created_at',
        'updated_at'
    ] 

@admin.register(Responsaveis)
class AdminResponsaveis(admin.ModelAdmin):
    fields = [
        'title',
        'users',
        'conta'
    ]
    list_display = [
        'id',
        'title',
        'get_users',
        'conta'
    ] 
