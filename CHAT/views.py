from django.shortcuts import render
from django.shortcuts import render, redirect
from CHAT.models import Chat
from MAIN.models import *
from playsound import playsound


r=0
def index(request,pk):
    if request.session.has_key('email'):
        email = request.session['email']
        index.p=pk
        p=pk
        global r 
        r=p

        
        te=Users.objects.get( email = email)
        tec=te.account
       
        if tec == "teacher":

            ch=ConfirmedList.objects.get(pk=r)
            rec=ch.appliedby
            dta=Chat.objects.filter( sender = email,reciever = rec)
            dta2=Chat.objects.filter( sender = rec,reciever = email)
        else:
            
            ch=AppliedList.objects.get(pk=r)
            rec=ch.appliedby
            dta=Chat.objects.filter( sender = email,reciever = rec)
            dta2=Chat.objects.filter( sender = rec,reciever = email)

       
        



        con={
            'data':dta,
            'data2':dta2,
            
        }

        return render(request,"chat/index.html",con)






def index2(request):
    if request.session.has_key('email'):
        email = request.session['email']
        global r 
        ch=AppliedList.objects.get(pk=r)
        rec=ch.appliedby
        dta=Chat.objects.filter( sender = email,reciever = rec)
        dta2=Chat.objects.filter( sender = rec,reciever = email)
       
        
        con={
            'data':dta,
            'data2':dta2,
            
        }


        return render(request,"chat/index.html",con)

def index3(request):
    if request.session.has_key('email'):
        email = request.session['email']
        global r 
        ch=ConfirmedList.objects.get(pk=r)
        rec=ch.appliedby
        dta=Chat.objects.filter( sender = email,reciever = rec)
        dta2=Chat.objects.filter( sender = rec,reciever = email)
       
        
        con={
            'data':dta,
            'data2':dta2,
            
        }


        return render(request,"chat/index.html",con)






def msg(request):
    if request.session.has_key('email'):
        email = request.session['email']
        global r
        i=r
        te=Users.objects.get( email = email)
        tec=te.account
       
        if tec == "student":
            ch=AppliedList.objects.get(pk=i)
            rec=ch.appliedby
            if request.method == 'POST':
              msg = request.POST['msg']
              sender=email
              ms=Chat.objects.create(sender=sender,reciever=rec,message=msg)
              return redirect('/CHAT/index2/')



        else:

            ch=ConfirmedList.objects.get(pk=i)
            rec=ch.appliedby
            if request.method == 'POST':
                msg = request.POST['msg']
                sender=email
                ms=Chat.objects.create(sender=sender,reciever=rec,message=msg)
                return redirect('/CHAT/index3/')

      
        






