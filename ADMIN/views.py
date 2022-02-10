from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

from MAIN.models import ForApproval, Studentdata, Tutordata, Users

# Create your views here.
def admlogin(request):
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
        return redirect("/ADMIN/Approveuser")
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


def Deleteuser(request):
    if request.session.has_key('email'):
        email = request.session['email']
        tutdata=Tutordata.objects.all()
        studdata=Studentdata.objects.all()
        con={
            'data':tutdata,
            'sdata':studdata
             }
            #  http://127.0.0.1:8000/ADMIN/Deleteuser/
        
        return render(request,'admin/removeorder.html',con)

def Deletestudent(request):
    if request.session.has_key('email'):
        email = request.session['email']
        studdata=Studentdata.objects.all()
        con={
            'sdata':studdata
             }
            #  http://127.0.0.1:8000/ADMIN/Deletestudent/
        
        return render(request,'admin/removestudent.html',con)

def userdelete(request,pk):
     if request.session.has_key('email'):
        email = request.session['email']
        # obj = Studentdata.objects.filter(pk=pk)
      
       
        obj5 = Tutordata.objects.get(pk=pk)
        mail=obj5.email
        obj1= Users.objects.get(email=mail)
        obj5.delete()
        obj1.delete()
        return redirect('/ADMIN/Deleteuser/')


def studelete(request,pk):
     if request.session.has_key('email'):
        email = request.session['email']
        # obj = Studentdata.objects.filter(pk=pk)
      
       
        obj5 = Studentdata.objects.get(pk=pk)
        mail=obj5.email
        obj1= Users.objects.get(email=mail)
        obj5.delete()
        obj1.delete()
        return redirect('/ADMIN/Deletestudent/')
    
def Approveuser(request):
    if request.session.has_key('email'):
        email = request.session['email']
        tutdata=ForApproval.objects.all()
        con={
            'data':tutdata
                }
        
        return render(request,'admin/order.html',con)

def approved(request,pk):
     if request.session.has_key('email'):
        email = request.session['email']
        # obj = Studentdata.objects.filter(pk=pk)
        obj1= ForApproval.objects.get(pk=pk)
        create=Tutordata.objects.create(name=obj1.name,email=obj1.email,medium=obj1.medium ,subjects=obj1.subjects,cls=obj1.cls,salary=obj1.salary,location=obj1.location, tutorimg=obj1.tutorimg, certificate1=obj1.certificate1,certificate2=obj1.certificate2,address=obj1.address,institute=obj1.institute, phone=obj1.phone,gender=obj1.gender,account=obj1.account) 
        users = Users.objects.create(account=obj1.account,name=obj1.name, email=obj1.email, phone=obj1.phone, password = obj1.password,gender=obj1.gender)
        create.save()
        users.save()
        obj5 = ForApproval.objects.filter(pk=pk)
        obj5.delete()
        return redirect('/ADMIN/Approveuser')
def disapprove(request,pk):
     if request.session.has_key('email'):
        email = request.session['email']
        # obj = Studentdata.objects.filter(pk=pk)
        obj5 = ForApproval.objects.filter(pk=pk)
        obj5.delete()
        return redirect('/ADMIN/Approveuser')
def admaddtutor(request):
    return render(request,'admin/admaddteacher.html')

def tutoradd(request):
     if request.session.has_key('email'):
        email = request.session['email']
        if request.method == 'POST':
           
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['mobile']
            gender=request.POST['gender']
            password1 = request.POST['password']
            t="teacher"
            tutimg=request.FILES.get('profilepic') 
            address=request.POST['address'] 
            email=request.POST['email'] 
            institute=request.POST['inst_nm'] 
            medium=request.POST['medium']
            subject=request.POST['Subjects']
            cls=request.POST['class']
            sal=request.POST['sal_range']
            loc=request.POST['location']
            cert1=request.FILES.get('cert1')
            cert2=request.FILES.get('cert2')
            apply=ForApproval.objects.get( email = email)
            apply.medium=medium
            apply.subjects=subject
            apply.cls=cls
            apply.salary=sal
            apply.location=loc
            apply.tutorimg=tutimg
            apply.certificate1=cert1
            apply.certificate2=cert2
            apply.address=address
            apply.institute=institute
            apply.save()
            users = Users.objects.create(account=t,name=name, email=email, phone=phone, password = password1)

            users.save()



        
    

