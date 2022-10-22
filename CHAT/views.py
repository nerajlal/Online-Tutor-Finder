from django.dispatch import receiver
from django.shortcuts import render
from django.shortcuts import render, redirect
from CHAT.models import Chat
from MAIN.models import *
from playsound import playsound


ids=[]
r=0
em=0
cn=0
def index(request,pk):
    if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
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
            mge={

            }
    
            for ii in dta:
                mge[ii.id]=[ii.sendername]
                mge[ii.id].append(ii.message)
                d=str(ii.date)
                ddate=d[0:19]
                mge[ii.id].append(ddate)

            for jj in dta2:
                mge[jj.id]=[jj.sendername]
                mge[jj.id].append(jj.message)
                d=str(jj.date)
                ddate=d[0:19]
                mge[jj.id].append(ddate)
            mge1={}   

            for i in sorted(mge):
                mge1[i]=[mge[i]]
            


            

            
        else:
            
            ch=AppliedList.objects.get(pk=r)
            rec=ch.appliedby
            dta=Chat.objects.filter( sender = email,reciever = rec)
            dta2=Chat.objects.filter( sender = rec,reciever = email)

            mge={

            }
    
            for ii in dta:
                mge[ii.id]=[ii.sendername]
                mge[ii.id].append(ii.message)
                d=str(ii.date)
                ddate=d[0:19]
                mge[ii.id].append(ddate)

            for jj in dta2:
                mge[jj.id]=[jj.sendername]
                mge[jj.id].append(jj.message)
                d=str(jj.date)
                ddate=d[0:19]
                mge[jj.id].append(ddate)
            mge1={}   

            for i in sorted(mge):
                mge1[i]=[mge[i]]



        # con={
        #     'data':dta,
        #     'data2':dta2,
            
            
            
        # }

        return render(request,"chat/index.html",{'mge':mge1,"dta":te})






def index2(request):
    if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
        global r 
        ch=AppliedList.objects.get(pk=r)
        rec=ch.appliedby
        dta=Chat.objects.filter( sender = email,reciever = rec)
        dta2=Chat.objects.filter( sender = rec,reciever = email)
        mge={

            }
       
        for ii in dta:
            mge[ii.id]=[ii.sendername]
            mge[ii.id].append(ii.message)
            d=str(ii.date)
            ddate=d[0:19]
            mge[ii.id].append(ddate)

        for jj in dta2:
            mge[jj.id]=[jj.sendername]
            mge[jj.id].append(jj.message)
            d=str(jj.date)
            ddate=d[0:19]
            mge[jj.id].append(ddate)
            # print(ii.id)
            # print(ii.sender)
            # print(ii.message)
            
                
               
            d=str(ii.date)
            ddate=d[0:19]
        mge1={}   

        for i in sorted(mge):
            mge1[i]=[mge[i]]

        print(mge1)  

       
        
        # con={
        #     'data':dta,
        #     'data2':dta2,
            
        # }


        return render(request,"chat/index.html",{'mge':mge1,"dta":te})

def index3(request):
    if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
        global r 
        ch=ConfirmedList.objects.get(pk=r)
        rec=ch.appliedby
        dta=Chat.objects.filter( sender = email,reciever = rec)
        dta2=Chat.objects.filter( sender = rec,reciever = email)
       
        mge={

            }
    
        for ii in dta:
            mge[ii.id]=[ii.sendername]
            mge[ii.id].append(ii.message)
            d=str(ii.date)
            ddate=d[0:19]
            mge[ii.id].append(ddate)

        for jj in dta2:
            mge[jj.id]=[jj.sendername]
            mge[jj.id].append(jj.message)
            d=str(jj.date)
            ddate=d[0:19]
            mge[jj.id].append(ddate)
        mge1={}   

        for i in sorted(mge):
            mge1[i]=[mge[i]]

       
        
        # con={
        #     'data':dta,
        #     'data2':dta2,
            
        # }



        return render(request,"chat/index.html",{'mge':mge1,"dta":te})






def msg(request):
    if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
        global r
        i=r
        te=Users.objects.get( email = email)
        tec=te.account
        nm=te.name
       
        if tec == "student":
            ch=AppliedList.objects.get(pk=i)
            rec=ch.appliedby
            if request.method == 'POST':
              msg = request.POST['msg']
              sender=email
              ms=Chat.objects.create(sender=sender,reciever=rec,message=msg,sendername=nm)
              return redirect('/CHAT/index2/')



        else:

            ch=ConfirmedList.objects.get(pk=i)
            rec=ch.appliedby
            if request.method == 'POST':
                msg = request.POST['msg']
                sender=email
                ms=Chat.objects.create(sender=sender,reciever=rec,message=msg,sendername=nm)
                return redirect('/CHAT/index3/')


                










def chatNotification(request):
    if request.session.has_key('email'):
        email = request.session['email']
        rec=Chat.objects.filter(reciever=email)
        c=str(rec)
        if c == "<QuerySet []>":
            q="YES"
        else:
            q="NO"

        con={
            "rec":rec,
            "q":q
        }
        return render(request,"chat/chatnotification.html",con)



def chatFromnotification(request,pk):
      if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
        tec=te.account
        global cn
        cn=pk
        if tec == "teacher":

            ch=Chat.objects.get(pk=pk)
            rec=ch.sender
            print(rec)
            dta=Chat.objects.filter( sender = email,reciever = rec)
            dta2=Chat.objects.filter( sender = rec,reciever = email)
            mge={

            }
    
            for ii in dta:
                mge[ii.id]=[ii.sendername]
                mge[ii.id].append(ii.message)
                d=str(ii.date)
                ddate=d[0:19]
                mge[ii.id].append(ddate)

            for jj in dta2:
                mge[jj.id]=[jj.sendername]
                mge[jj.id].append(jj.message)
                d=str(jj.date)
                ddate=d[0:19]
                mge[jj.id].append(ddate)
            mge1={}   

            for i in sorted(mge):
                mge1[i]=[mge[i]]
            


            
        else:
            
            ch=Chat.objects.get(pk=pk)
            rec=ch.sender
            
            dta=Chat.objects.filter( sender = email,reciever = rec)
            dta2=Chat.objects.filter( sender = rec,reciever = email)
            print(rec,email)


            mge={

            }
    
            for ii in dta:
                mge[ii.id]=[ii.sendername]
                mge[ii.id].append(ii.message)
                d=str(ii.date)
                ddate=d[0:19]
                mge[ii.id].append(ddate)

            for jj in dta2:
                mge[jj.id]=[jj.sendername]
                mge[jj.id].append(jj.message)
                d=str(jj.date)
                ddate=d[0:19]
                mge[jj.id].append(ddate)
            mge1={}   

            for i in sorted(mge):
                mge1[i]=[mge[i]]



        # con={
        #     'data':dta,
        #     'data2':dta2,
            
            
            
        # }

        return render(request,"chat/index2.html",{'mge':mge1,"dta":te})


def msg2(request):
    if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
        global r
        i=r
        global cn
        te=Users.objects.get( email = email)
        tec=te.account
        nm=te.name
       
        # if tec == "student":
        ch=Chat.objects.get(pk=cn)
        rec=ch.sender
        if request.method == 'POST':
            msg = request.POST['msg']
            sender=email
            ms=Chat.objects.create(sender=sender,reciever=rec,message=msg,sendername=nm)
            return redirect('/CHAT/index4/')



        # else:

        #     ch=Chat.objects.get(pk=cn)
        #     rec=ch.sender
        #     if request.method == 'POST':
        #         msg = request.POST['msg']
        #         sender=email
        #         ms=Chat.objects.create(sender=sender,reciever=rec,message=msg,sendername=nm)
        #         return redirect('/CHAT/index3/')
        






def index4(request):
    if request.session.has_key('email'):
        email = request.session['email']
        te=Users.objects.get( email = email)
        global cn 
        # ch=AppliedList.objects.get(pk=r)
        ch=Chat.objects.get(pk=cn)
        rec=ch.sender
        dta=Chat.objects.filter( sender = email,reciever = rec)
        dta2=Chat.objects.filter( sender = rec,reciever = email)
        mge={

            }
       
        for ii in dta:
            mge[ii.id]=[ii.sendername]
            mge[ii.id].append(ii.message)
            d=str(ii.date)
            ddate=d[0:19]
            mge[ii.id].append(ddate)

        for jj in dta2:
            mge[jj.id]=[jj.sendername]
            mge[jj.id].append(jj.message)
            d=str(jj.date)
            ddate=d[0:19]
            mge[jj.id].append(ddate)
            # print(ii.id)
            # print(ii.sender)
            # print(ii.message)
            
                
               
            d=str(ii.date)
            ddate=d[0:19]
        mge1={}   

        for i in sorted(mge):
            mge1[i]=[mge[i]]

        print(mge1)  

       
        
        # con={
        #     'data':dta,
        #     'data2':dta2,
            
        # }


        return render(request,"chat/index2.html",{'mge':mge1,"dta":te})





