from django.contrib import admin
from .models import Pix

# Register your models here.

@admin.register(Pix)
class PixAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'chave_pix',
        'cidade',
        'user_id'
    ]

    list_display = [
        'id',
        'nome',
        'chave_pix',
        'cidade',
        'user_id',
    ]