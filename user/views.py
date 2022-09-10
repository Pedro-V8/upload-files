from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from .forms import UserForm
from django.contrib.auth.models import auth

from upload.views import index
# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request , user)
            messages.success(request, "Registro bem sucedido")
            return HttpResponseRedirect('')
        messages.error(request, "Unsuccessful registration. Invalid information.")
        print('------------------------')
        print("ERROR")

    else: 
        form = UserForm()
        return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)
        '''print(user)
        return "OK"'''
        if user is not None:
            auth.login(request , user)
            return redirect('uploadFile')
        else:
            messages.info(request , 'Invalid Username or Password, try again...')
            return render(request , 'login.html')
    else:
        return render(request , 'login.html')




