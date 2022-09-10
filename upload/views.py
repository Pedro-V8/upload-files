from django.shortcuts import render

from .models import Document , Transacao
from user.models import Profile
from .services.trata_archive import retorna_data

import codecs

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("--------------------------------")
        print(request)

        fileTitle = request.POST["fileTitle"]
        uploaded_file = request.FILES["uploadedFile"]
        uploaded_file_utf_8 = codecs.EncodedFile(uploaded_file, "utf-8")


        document = Document(
            title = fileTitle,
            uploadedFile = uploaded_file
        )
        document.save()
        documento = Document.objects.get(title=fileTitle)

        #f = document.uploadedFile
        lines = uploaded_file_utf_8.open('r',).readlines()
        primeira_data = retorna_data(lines[0])
        #print(primeira_data)
        for line in lines:
            dia_transacao = retorna_data(line)
            if dia_transacao == primeira_data:
                data = str(line).split(',')
                data[7] = data[7].strip()

                transacao = Transacao(
                    banco_origem = data[0][2:],
                    agencia_origem = data[1],
                    conta_origem = data[2],
                    banco_destino = data[3],
                    agencia_destino = data[4],
                    conta_destino = data[5],
                    valor_transacao = float(data[6]),
                    data_hora = data[7][0:19],
                    upload_id = documento    
                )
                transacao.save()

    user = Profile.objects.get(email=request.user)
    documents = Document.objects.filter(user_id=user.id)

    return render(request , "index.html", context= {
      "files": documents,
       "user": user
    })

def retrieve_file(request , pk):
    if request.method == "GET":

        document = Document.objects.get(id=pk)
        transacoes = Transacao.objects.filter(upload_id=document)
        print("#####################################")
        print(transacoes)
        
        return render(request , "retrieve.html" , context={
            "transactions": transacoes
        })


'''def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = UploadFileForm()
'''


