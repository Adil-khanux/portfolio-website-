from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact

# Create your views here.

# def home(request):
#      return render(request,'home.html')

def contact(request):
     if request.method=='POST':
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        print(name,email,phone,message)

# apply conditions
        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and less 30 words')
            return render (request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'Invalid email try again ')
            return render (request,'home.html')
            
        if len(phone)>1 and len(phone)<30:
            pass
        else:
            messages.error(request,'Invalid number try again')
            return render (request,'home.html')
        
        user=models.Contact(name=name,email=email,phone=phone,message=message)
        user.save()
        messages.success(request,"Thank you for connecting me  || your message have been saved")
        print('data has been save to database')

    
     return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def skill(request):
    return render(request,'skills.html')

def home(request):
    if request.method=='POST':
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        print(name,email,phone,message)

# apply conditions
        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and less 30 words')
            return render (request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'Invalid email try again ')
            return render (request,'home.html')
            
        if len(phone)>1 and len(phone)<30:
            pass
        else:
            messages.error(request,'Invalid number try again')
            return render (request,'home.html')
        
        user=models.Contact(name=name,email=email,phone=phone,message=message)
        user.save()
        messages.success(request,"Thank you for connecting me  || your message have been saved")
        print('data has been save to database')

    return render (request,'home.html')
