from pydoc import Doc
from turtle import title
from django.shortcuts import render

from .models import Document
from .services.trata_archive import retorna_data

import codecs

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("--------------------------------")

        fileTitle = request.POST["fileTitle"]
        uploaded_file = request.FILES["uploadedFile"]
        uploaded_file_utf_8 = codecs.EncodedFile(uploaded_file, "utf-8")


        document = Document(
            title = fileTitle,
            uploadedFile = uploaded_file
        )

        #f = document.uploadedFile
        lines = uploaded_file_utf_8.open('r',).readlines()
        primeira_data = retorna_data(lines[0])
        
        for line in lines:
            data = retorna_data(line)

            if data == primeira_data:

                print("SIM")
            else:
                print("NAO")



        #document.save()
    documents = Document.objects.all()
    return render(request , "index.html", context= {
        "files": documents
    })

def retrieve_file(request , pk):
    if request.method == "GET":
        try:
            document = Document.objects.get(id=pk)
        
            return render(request , "retrieve.html" , context={
                "file": document
            })
        except:
            documents = Document.objects.all()
            return render(request , "index.html", context= {
                "files": documents
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


