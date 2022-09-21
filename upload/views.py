from django.shortcuts import render

from .models import Conta 
from user.models import Profile
from .services.trata_archive import retorna_data

import codecs

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("!!!!!!!!!!!!!!!!!!!!!")
        print(request.POST)
        #return "OK"


        conta = Conta(
            title = request.POST["title"],
            empresa = request.POST["empresa"],
            status = request.POST.get('status'),
            imagem = request.FILES["uploadedFile"],
            data_emissao = request.POST['data_emissao'],
            data_validade = request.POST['data_validade'],
            user_id = request.user
        )
        conta.save()
    
    user = Profile.objects.get(email=request.user)
    contas = Conta.objects.all()
    return render(request , "index.html", context= {
        "contas": contas,
        "user": user
    })

def retrieve_file(request , pk):
    if request.method == "GET":
        try:
            
            conta = Conta.objects.get(id=pk)
            print(conta.user_id)
            return render(request , "retrieve.html" , context={
                "conta": conta
            })
        except:
            return index(request)


'''def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = UploadFileForm()
'''


