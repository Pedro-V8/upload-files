from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def pagar(request):

    return render(request , "pagar.html")

@login_required(login_url='/login')
def cadastrar_pix(request):
    if request.method == 'POST':
        print("$$$$$$$$$$$$$$$$$$")
        print("OI")
        return "OK"
    return render(request , "cadastrar_pix.html")
    