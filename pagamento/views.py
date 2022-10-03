from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Pix

# Create your views here.

@login_required(login_url='/login')
def pagar(request):

    return render(request , "pagar.html")

@login_required(login_url='/login')
def cadastrar_pix(request):
    if request.method == 'POST':
        conta_pix = Pix(
            nome = request.POST["nome_completo"],
            chave_pix = request.POST["chave_pix"],
            cidade = request.POST["cidade"],
            user_id = request.user

        )
        conta_pix.save()
        print(request.POST["chave_pix"])
        return redirect('uploadFile')
    return render(request , "cadastrar_pix.html")
    