from errno import EMLINK
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import ConfirmedList, Studentdata, Users,AppliedList,ForApproval,Tutordata
from .models import Tutioninfo
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from datetime import datetime
import random
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# from .forms import StudentForm
  
# import crypt
def index(request):
     if request.session.has_key('email'):
        email = request.session['email']
        data=Users.objects.get(email=email)
        if data.account=="teacher":
            return redirect("/index1")
        else:
            return render(request,"index1.html")
       
     else:
       
        return render(request,"index1.html")  
    

def index1(request):
    if request.session.has_key('email'):
        email = request.session['email']
        studdata=Studentdata.objects.all()
        ad=AppliedList.objects.filter(appliedby=email)
        wm=[]
        stu=[]
        for q in studdata:
            stu.append(q.email)

        for i in ad:
            wm.append(i.student)

        count=[]
        for i in studdata:
            if i.email in wm:
                count.append("Y")
            else:
                count.append("N")

        mylist = zip(studdata, count)
       
        con={
                'data':studdata,
                'addata':ad,
                'c':mylist,
                'wm':wm
            }
        return render(request,"index.html",con)
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     


def about(request):
    return render(request,"aboutme.html")
def register(request):
    return render(request,'registration.html')


def register_user(request):
    if request.method == 'POST':
        typeuser=request.POST['account']
        email = request.POST['email']
        if Users.objects.filter(email=email).exists():
            messages.success(request,"e-mail already exists")
            return render(request,'registration.html')
        else:
            if typeuser=="student":
                typeuser=request.POST['account']
                name = request.POST['name']
                email = request.POST['email']
                phone = request.POST['mobile']
                gender=request.POST['gender']
                password1 = request.POST['password']
                t=typeuser
                # password_hash = crypt.crypt(password1)
                # password2 = request.POST['cpassword']
                users = Users.objects.create(account=typeuser,name=name, email=email, 
                                                phone=phone, password = password1,gender=gender)
                users.save()
                # if typeuser=="student":
                request.session['email'] = email
                return redirect("/studentdata")
            # To check the password.
            # valid_password = crypt.crypt(cleartext, password_hash) == password_hash
            
            else:
                typeuser=request.POST['account']
                name = request.POST['name']
                email = request.POST['email']
                phone = request.POST['mobile']
                gender=request.POST['gender']
                password1 = request.POST['password']
                t=typeuser
                # password_hash = crypt.crypt(password1)
                # password2 = request.POST['cpassword']
                users =ForApproval.objects.create(account=typeuser,name=name, email=email, 
                                                phone=phone, password = password1,gender=gender)
                users.save()
            
            
                return render(request, "updatetutorinfo.html")




    else:
        return render(request, 'aboutme.html')






def login(request):
    return render(request,"login.html")

def user_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        m =Users.objects.get(email=request.POST['email'])
        if m.password == request.POST['password']:
            request.session['email'] = m.email
            if m.account=="teacher":
                studdata=Studentdata.objects.all()
                con={
                    'data':studdata
                }
                        
                return redirect("/index1")
            else:
                return redirect("/profile")
        else:
            return HttpResponse("Your username and password didn't match.")



        # # user = authenticate(username=email, password=password)
        # if user is not None:
        #      print("login sucessfull")
        #      return render(request, 'aboutme.html')
        # else:
        #     print("login failed")
        #     return HttpResponse('aboutme.html')
        
def formView(request): 
    if request.session.has_key('email'):
        studentname = request.session['email']  
        studdata=Studentdata.objects.filter(email=studentname)
        con={
            'data':studdata
        }
        return render(request,"studentpost.html",con)
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     

      
# def admlogin(request):
#     return render(request,'admin/Login.html')
def tutioninfo(request):
    return render(request,"updatetutioninfo.html")

def tutiondata(request):   
        g=request.POST.getlist('sub_list[]')
        stud= request.session['email']  
        medium=request.POST.getlist('medium_list[]')
        subject=request.POST.getlist('sub_list[]')
        cls=request.POST.getlist('class_list[]')
        sal=request.POST['sal_range']
        loc=request.POST['location']
        separator = ", "
        lisub=separator.join(map(str, subject))
        licls=separator.join(map(str, cls))
        limed=separator.join(map(str, medium))
        # lisub = str(subject)[1:-1]
        # info=Tutioninfo.objects.create(email=stud,medium=medium ,subjects=subject,cls=cls,salary=sal,location=loc)
        # info.save()
        email = request.session['email']
        Studentdata.objects.filter( email = email).update(medium=limed ,subjects=lisub,cls=licls,salary=sal,location=loc)
        return redirect('/formView')







def postdata(request):
    if request.session.has_key('email'): 
       email = request.session['email']
       name = Users.objects.get( email = email)
       con={
            'data':name
        }
        # return render(request,"postform.html")
       return render(request,"postform.html", con)
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     


def studentdata(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        con={
            'data':dta
        }
        return render(request,"updateinfo.html",con)
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     

# def studentinput(request):
#     context ={}
  
#     # create object of form
#     form = StudentForm(request.POST or None, request.FILES or None)
      
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
  
#     context['form']= form
#     return redirect('/formView')

def studentinput(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        gender=dta.gender
        name=dta.name
        img=request.FILES.get('profilepic') 
        address=request.POST.get('address') 
        phone=request.POST['phone']
        institute=request.POST['inst_nm'] 
        deadline=request.POST['deadline'] 
        info=Studentdata.objects.create(email=email,name=name,gender=gender,proimg=img,address=address,institute=institute,phone=phone,deadline=deadline)
        info.save()
        return redirect('/uptution')
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     
def poststudent(request):
    studdata=Studentdata.objects.all()
    con={
            'data':studdata
        }
    return render(request,"index.html",con)


def uptution(request):
    return render(request,"updatetutioninfo.html")



def notification(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        g=dta.account
        if g=="student":
            obj = AppliedList.objects.filter(student=email)
            c=str(obj)
            
            if c == "<QuerySet []>":
                q="YES"
            else:
                q="NO"
            con={
                "data":dta,

                "applied":obj,
                "q":q
            }
            return render(request,"notification.html",con)

        else:
            obj = ConfirmedList.objects.filter(teacher=email)
            c=str(obj)
            
            if c == "<QuerySet []>":
                q="YES"
            else:
                q="NO"
            con={
                "data":dta,

                "applied":obj,
                "q":q
            }
            return render(request,"teachernotification.html",con)
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     






def apply(request,pk):
    if request.session.has_key('email'):
        email = request.session['email']
        obj = Studentdata.objects.filter(pk=pk)
        obj2=Tutordata.objects.get(email=email)
        obj1 = Studentdata.objects.get(pk=pk)
        mail=obj1.email
        apname=obj2.name
        apply = AppliedList.objects.create(student=mail,appliedby=email,appliedname=apname) 
        apply.save()
        return redirect('/index1')
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     
    
def profile(request):
     if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        g=dta.account
        if g=="student":
            obj=Studentdata.objects.filter(email=email)
            obj1=Studentdata.objects.get(email=email)

            con={
                "data":obj1,
                "g":g
            }
        else:
            obj1=Tutordata.objects.get(email=email)
            con={
                "data":obj1,
                "g":g
                
            }

        return render(request,'profile.html',con)
     else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     


def tutordata(request):
     if request.method == 'POST':
        tutimg=request.FILES.get('profilepic') 
        address=request.POST['address'] 
        email=request.POST['email'] 
        # phone=request.POST['phone']
        institute=request.POST['inst_nm'] 
        medium=request.POST['medium']
        subject=request.POST['Subjects']
        cls=request.POST['class']
        sal=request.POST['sal_range']
        loc=request.POST['location']
        cert1=request.FILES.get('cert1')
        cert2=request.FILES.get('cert2')
        # apply =ForApproval.objects.create(email="hgv",phone="234",medium=medium ,subjects=subject,cls=cls,salary=sal,location=loc, tutorimg=tutimg, certificate1=cert1,certificate2=cert2,address=address,institute=institute) 
        # apply.save()
        # apply=ForApproval.objects.filter( email = email).update(medium=medium ,subjects=subject,cls=cls,salary=sal,location=loc, tutorimg=tutimg, certificate1=cert1,certificate2=cert2,address=address,institute=institute)
        # apply.save()
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
        messages.info(request,"Registration successfull Wait for admin approval")
        return render(request,'registration.html')
    


def editstudent(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        con={
            'data':dta
        }

        return render(request,'editstudent.html',con)
        
        
def studentedit(request):
    if request.session.has_key('email'):
        email = request.session['email']
        g=request.POST.getlist('sub_list[]')
        stud= request.session['email']  
        medium=request.POST.getlist('medium_list[]')
        subject=request.POST.getlist('sub_list[]')
        cls=request.POST.getlist('class_list[]')
        sal=request.POST['sal_range']
        loc=request.POST['location']
        separator = ", "
        lisub=separator.join(map(str, subject))
        licls=separator.join(map(str, cls))
        limed=separator.join(map(str, medium))
        # lisub = str(subject)[1:-1]
        # info=Tutioninfo.objects.create(email=stud,medium=medium ,subjects=subject,cls=cls,salary=sal,location=loc)
        # info.save()
        email = request.session['email']
        Studentdata.objects.filter( email = email).update(medium=limed ,subjects=lisub,cls=licls,salary=sal,location=loc)
        return redirect('/profile')
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     

def personalstuddata(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        con={
            'data':dta
        }
        return render(request,"updatepersonaldata.html",con)
        

def updatepersonal(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Users.objects.get( email = email)
        gender=dta.gender
        name=dta.name
        address=request.POST.get('address') 
        phone=request.POST['phone']
        institute=request.POST['inst_nm'] 
        deadline=request.POST['deadline'] 
        Studentdata.objects.filter( email = email).update(email=email,name=name,gender=gender,address=address,institute=institute,phone=phone,deadline=deadline)
       
        return redirect('/profile')

def viewteacher(request,pk):
     if request.session.has_key('email'):
        email = request.session['email']
        obj1= AppliedList.objects.get(pk=pk)
        obj3= Studentdata.objects.get(email=email)
        mail=obj1.appliedby
        obj2= Tutordata.objects.get(email=mail)
        con={
            "data":obj2,
            "dta":obj3
        }
        return render(request,'viewteacher.html',con)



def confirmteacher(request,pk):
    if request.session.has_key('email'):
        email = request.session['email']
        obj = Tutordata.objects.filter(pk=pk)
        obj2=Studentdata.objects.get(email=email)
        obj1 = Tutordata.objects.get(pk=pk)
        mail=obj1.email
        apname=obj2.name
        apply = ConfirmedList.objects.create(teacher=mail,appliedby=email,appliedname=apname) 
        apply.save()
        return redirect('/notification')
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     



def personaltutordata(request):
    if request.session.has_key('email'):
        email = request.session['email']
        dta=Tutordata.objects.get( email = email)
        con={
            'data':dta
        }
        return render(request,'edittutor.html',con)
    else:
        return HttpResponse("<h1>Server error Please login to return to this page<h1> ")
     



def editteacher(request):
    if request.session.has_key('email'):
        mail = request.session['email']
        dta=Users.objects.get( email = mail)
        dta2=Tutordata.objects.get( email = mail)
        c1=dta2.certificate1
        c2=dta2.certificate2
        c3=dta2.tutorimg
        if request.method == 'POST':
            tutimg=request.FILES.get('profilepic') 
            address=request.POST['address'] 
            email=mail
            # phone=request.POST['phone']
            institute=request.POST['inst_nm'] 
            medium=request.POST['medium']
            subject=request.POST['Subjects']
            cls=request.POST['class']
            sal=request.POST['sal_range']
            loc=request.POST['location']
            cert1=request.FILES.get('cert1')
            cert2=request.FILES.get('cert2')
            # apply =ForApproval.objects.create(email="hgv",phone="234",medium=medium ,subjects=subject,cls=cls,salary=sal,location=loc, tutorimg=tutimg, certificate1=cert1,certificate2=cert2,address=address,institute=institute) 
            # apply.save()
            # apply=ForApproval.objects.filter( email = email).update(medium=medium ,subjects=subject,cls=cls,salary=sal,location=loc, tutorimg=tutimg, certificate1=cert1,certificate2=cert2,address=address,institute=institute)
            # apply.save()
            apply=Tutordata.objects.get( email = email)
            apply.medium=medium
            apply.subjects=subject
            apply.cls=cls
            apply.salary=sal
            apply.location=loc
            apply.address=address
           
           
       
       
            if cert1==None:
                apply.certificate1=c1
            else:
                 apply.certificate1=cert1

            if cert2==None:
                apply.certificate2=c2
            else:
                 apply.certificate2=cert2

            if tutimg==None:
                apply.tutorimg=c3
            else:
                 apply.tutorimg=tutimg

            apply.save()
            return redirect('/profile')

def resetpassword(request):
    email=request.POST['email']
    if Users.objects.filter(email=email).exists():
        # email="anandhua14@gmail.com"
        TO=email
        otp = random.randint(999,9999)
        global rp
        global eml 
        eml=email
        rp=otp

        stotp=str(otp)
        string="your One Time Password for resetting EDUCARE user password is "
        msgs=string+stotp+" And is only valid for 2 minutes"
        # print(type(msgs))
        send_mail(
                'EDUCARE Password reset OTP',
                "".join(msgs),
                'educaretutorfinder@gmail.com',
                [TO],
                
                fail_silently=False,
                        )
        return render(request,"reset.html")
    else:
        messages.success(request,"Unknown User e-mail id does not exist")
        return render(request,"settings.html")



def printpw(request):
   return render(request,"settings.html")




def changepwd(request):
    pwd1=request.POST['pwd1']
    pwd2=request.POST['pwd2']
    otp=request.POST['otp']
    global rp
    global eml
    if rp==int(otp):
        if pwd1==pwd2:
            cpwd=Users.objects.filter(email=eml).update(password=pwd1)
            return render(request,"login.html")
        else:
            messages.info(request,"passwords Does not match")
            return render(request,"reset.html")
    else:
        messages.info(request,"OTP doesnot match")
        return render(request,"reset.html")
def logout(request):
    if request.session.has_key('email'):
        request.session.flush()
        return redirect('/')
       

