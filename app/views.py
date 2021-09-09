from django.shortcuts import render,get_object_or_404,HttpResponse
from django.shortcuts import redirect
from .models import page,comment
from .forms import Registrationform,Myform,Editprofileform,commentform
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import  messages
#from django.template.loader import render_to_string

# Create your views here.
def home(request,*args,**kwargs):
    key=page.objects.all()
    return render(request,'home.html',{'key':key})

def jump(request,id):    
    upnext=get_object_or_404(page,id=id)
    msg=upnext.comment.all()
    com=commentform()
    if request.method=="POST":
        com=commentform(request.POST)
        coms=comment.objects.create(post=upnext,name=request.POST['name'],email=request.POST['email'],content=request.POST['content'])
        coms.save()
    else:
        com=commentform()    
    context={
        'upnext':upnext,
        'comment':msg,
        'commentform':com
    }
    return render(request, 'postdetails.html',context)

def Registration(request):
    form=Registrationform()
    if request.method=="POST":
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            mail=form.cleaned_data.get('email') 
            user=form.cleaned_data.get('username') 
            send_mail(
                'Registartion Successful', 
                'Dear ' +user+ ' your Account is created successfully on Free learn site.Happy for being part of our Family!!!',
                'djangot1798@gmail.com',
                 [mail],
                 fail_silently=False
                 )
           
            messages.success(request,'Your Account is Created ' + user +'.')
            return redirect('/login')
        else:
            form=Registrationform()
    return render(request,'registration/register.html',{'form':form})    
def LoginView(request):
    return render(request,'registration/login.html')  
@login_required
def profile(request):
    mine=Myform()
    key=page.objects.all()
    if request.method=="POST":
        mine=Myform(request.POST,request.FILES)
        if mine.is_valid():
            mine.save()
        else:
            mine=Myform()
    context={'mine':mine,'key':key}        
    return render(request,'profile.html',context)   

@login_required()
def editprofile(request):
    form=Editprofileform()
    if request.method=='POST':
        form=Editprofileform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:
            form=Editprofileform()
    return render(request,'edit.html',{'edit':form})
@login_required()
def delete(request,id):
    mine=Myform()
    key=page.objects.get(id=id)
    key.delete()
    
    return redirect('/profile')
@login_required()
def update(request,id):
    mine=Myform()
    update=page.objects.get(id=id)
    update=Myform(request.POST,request.FILES,instance=update)
    if update.is_valid():
        update.save()
        return redirect('/profile')
    return render(request,'update.html',{'update':update})    



def contact(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Subject=request.POST.get('Subject')
        Query=request.POST.get('Query')
        Phone=request.POST.get('Phone')
        #print(Name,Email,Query)
        email = EmailMessage(
            Subject,
            Query,
            Email,
            ['djangot1798@gmail.com']
            )

       # file=request.FILES['file']
       # email.attach(file.name,file.read(),file.content_type)

        email.send()
        messages.success(request,'Your Request Form is Submitted! ')
       # return HttpResponse('Sent')

    return render(request,'contact.html')

def About(request):
    return render(request, 'about.html')

def searchbar(request):
     search=request.GET.get('search')
     if search==None:
        search= page.objects.all()
     else:
         search=page.objects.filter(keyword=search)   

     return render(request,'search.html',{'search':search})    