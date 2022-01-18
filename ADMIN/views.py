from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

from MAIN.models import ForApproval

# Create your views here.
def admlogin(request):
    createAdmin()
    return render(request,'admin/Login.html')

def createAdmin():
    if not User.objects.filter(username='admin@admin').exists():
        createadmin = User.objects.create_user(username='admin@admin' , first_name='Admin', password='admin', is_superuser = 1)
        createadmin.save()
        
def adm(request):

    email=request.POST["email"]
    password=request.POST["password"]
    request.session['email'] = email
    user = authenticate(username=email, password=password)
    if user is not None:
        return redirect("/Approveuser")
    else:
        return render(request,'admin/login.html')
def admindex(request):
     return render(request,'admin/index.html')

def Approveuser(request):
    if request.session.has_key('email'):
        email = request.session['email']
        tutdata=ForApproval.objects.all()
        con={
            'data':tutdata
             }
        
        return render(request,'admin/order.html',con)
 
