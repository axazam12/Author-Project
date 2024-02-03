from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def Register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect(request,'register')
        
    return render(request,'auth/register.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('listbooks')
        else:
            messages.info(request,'please provide correct details')
            return redirect('login')



    return render(request,'auth/login.html')

def Logout(request):
    auth.logout(request)
    return redirect('listbooks')

