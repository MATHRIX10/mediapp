from django.shortcuts import render, HttpResponse , redirect
from .forms import LoginForm, UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required 
from .models import Profil

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

def register(request) :
    if request.method == 'POST' :
        # we have to get the data from the form 
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid() : 
            new_user = user_form.save(commit = False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            Profil.objects.create(user=new_user)
            return render(request, 'mediapp/register_done.html')
    else :
        user_form = UserRegistrationForm() 
    return render(request,'mediapp/register.html',{'user_form' : user_form})

@login_required
def edit(request) :
    if request.method == 'POST' :
        user_form = UserEditForm(instance = request.user, data = request.POST)
        profile_form  = ProfileEditForm(instance=request.user.profil, data = request.POST, files = request.FILES)

        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save() 
            profile_form.save() 

    else :
        user_form = UserEditForm(instance = request.user)
        profile_form  = ProfileEditForm(instance=request.user.profil, files = request.FILES)
    return render(request,'mediapp/edit.html',{'user_form':user_form,'profile_form':profile_form})



