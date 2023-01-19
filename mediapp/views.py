from django.shortcuts import render, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate , login


# Create your views here.



def userLogin(request) :

    if request.method == 'POST' :
        form = LoginForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data

            user = authenticate(request, username = data['username'] , password = data['password'])
            
            if user is not None :
                login(request,user)

                return HttpResponse("user authenticated and logged in ")

            else : 
                return HttpResponse('Invalid Login')

    else : 

        form = LoginForm() 
    return render(request,'mediapp/login.html',{'form':form})


def index(request) :
    return render(request, 'mediapp/index.html')