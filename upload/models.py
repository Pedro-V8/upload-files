from django.db import models
from django.utils import timezone
from user.models import Profile
# Create your models here.

def padrao():
    return 'Aberto'

def default_image(instance , filename):
    return f"media/contas/{filename}-JPG"
    
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Conta(Base):
    title = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    status = models.CharField(max_length=8 , default=padrao)
    imagem = models.ImageField(upload_to='contas')
    data_emissao = models.CharField(max_length=10)
    data_validade = models.CharField(max_length=11)
    valor = models.FloatField()

    user_id = models.ForeignKey(Profile , on_delete=models.CASCADE ,related_name='conta')

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

class Responsaveis(models.Model):
    title = models.CharField(max_length=200)
    users = models.ManyToManyField(Profile)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE , related_name='conta')

    class Meta:
        verbose_name = 'Resonsavel'
        verbose_name_plural = 'Responsaveis'

    def get_users(self):
        return ",".join([str(p) for p in self.users.all()])