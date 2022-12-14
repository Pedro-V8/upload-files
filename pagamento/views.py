from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Pix
from upload.models import Conta
from .pixqrcodegen import Payload

# Create your views here.

@login_required(login_url='/login')
def pagar(request , pk):
    nome_cidade = "Brasília"
    nomeTxtId = "FamíliaVieira"

    conta = Conta.objects.get(id=pk)
    pix_user = Pix.objects.get(user_id=conta.user_id)

    conta_title_formatado = conta.title.replace(" " , "")

    pay = Payload(
        pix_user.nome.replace(" " , ""), 
        pix_user.chave_pix, 
        str(conta.valor),
        nome_cidade,
        nomeTxtId, 
        conta_title_formatado
    )

    pay.gerarPayload()
    
    return render(request , "pagar.html" , context = {
        "url": f"../media/pixQrCode/{conta_title_formatado}QrCode.png"
    })

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
    