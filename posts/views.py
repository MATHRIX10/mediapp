from django.shortcuts import render
from .models import Post 
from .forms import PostCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required 
def post_create(request) :
    if request.method == 'POST' :
      

        form = PostCreationForm(data = request.POST,files=request.FILES)
        if form.is_valid() :
            new_item = form.save(commit=False)
            new_item.user = request.user 
            new_item.save(); 
            
        else :

            print('the form is not valid  \n\n\n\n\n')
            
   

    else :
        form = PostCreationForm(data=request.GET)
        

    return render(request,'posts/create.html',{'form':form})


def feed(request) : 
    # get all the posts form all the users 
    posts = Post.objects.all() 

    return render(request,'posts/feed.html',{'posts':posts})
