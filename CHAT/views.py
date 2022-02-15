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

        return render(request,"chat/index.html")

def index2(request):
    if request.session.has_key('email'):
        email = request.session['email']
        global r 
        return render(request,"chat/index.html")






def msg(request):
    if request.session.has_key('email'):
        email = request.session['email']
        global r
        i=r
        ch=AppliedList.objects.get(pk=i)
        rec=ch.appliedby
      
        if request.method == 'POST':
              msg = request.POST['msg']
              sender=email
              ms=Chat.objects.create(sender=sender,reciever=rec,message=msg)
              return redirect('/CHAT/index2/')






