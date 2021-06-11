from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if(password1==password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username Taken')
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email ID exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request,'Password wrong')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")

def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        flag=auth.authenticate(username=username,password=password)
        if(flag is not None):
            auth.login(request,flag)
            #messages.info(request,'Login Successful')
            return redirect('/') 
        elif(User.objects.filter(username=username).exists()):
            messages.info(request,'Password wrong')
            return redirect('login')
        else:
            return redirect('register')
        # if(User.objects.filter(username=username).exists()):
        #     if(password==User.objects.filter(username=password).get()):
        #         messages.info(request,'Login Successful')
        #         return redirect('/')                
            
        # else:
        #     return redirect('register')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')