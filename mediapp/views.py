from django.shortcuts import render, HttpResponse , redirect
from .forms import LoginForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required 

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

@login_required
def index(request) :
    if  not request.user.is_authenticated :
        return redirect('mediapp/login.html')

    return render(request, 'mediapp/index.html')