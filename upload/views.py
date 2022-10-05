import email
from django.shortcuts import render

from .models import Conta , Responsaveis
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView

# Create your views here.

@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        users = []
        emails = request.POST.getlist('check')

        if not emails:
            users.append(request.user)
        else:
            users = Profile.objects.filter(email__in=emails)

        print(users)
        return "OK"


        conta = Conta(
            title = request.POST["title"],
            empresa = request.POST["empresa"],
            imagem = request.FILES["uploadedFile"],
            data_emissao = request.POST['data_emissao'],
            data_validade = request.POST['data_validade'],
            valor = request.POST["valor"],
            user_id = request.user
        )

        conta.save()

        title_r = 'responsaveis_{}'.format(request.POST["title"].replace(" " , "_"))

        responsaveis_conta = Responsaveis(
            title = title_r,
            conta = conta
        )
        responsaveis_conta.save()

        for user in users:
            responsaveis_conta.users.add(user)


    
    user = Profile.objects.get(email=request.user)
    users = Profile.objects.all()
    contas = Conta.objects.all()

    return render(request , "index.html", context= {
        "user": user,
        "users": users,
        "contas": contas,
        
    })

@login_required(login_url='/login')
def retrieve_file(request , pk):
    if request.method == "GET":
        try:

            conta = Conta.objects.get(id=pk)
            user = Profile.objects.get(conta=conta)
            responsaveis = Responsaveis.objects.get(conta=conta)
            print("$$$$$$$$$$$$$$$$$$$")
            print(responsaveis.users.all())

            return render(request , "retrieve.html" , context={
                "conta": conta,
                "user":user,
                "responsaveis": responsaveis.users.all()
            })
        except:
            return index(request)

@login_required(login_url='/login')
def delete_file(request , pk):
    if request.method == "GET":
        conta = Conta.objects.get(id=pk)
        
        if conta:
            conta.delete()

            return index(request)
