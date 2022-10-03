from django.db import models
from user.models import Profile

# Create your models here.

class Pix(models.Model):
    nome = models.CharField(max_length=200)
    chave_pix = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE , related_name='pix')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
