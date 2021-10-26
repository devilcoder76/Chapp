from django.shortcuts import redirect, render
from . import models
from django.db.models import Q
# Create your views here.

def chat(request,res):
    if request.session.has_key('username'):
        if request.method=='POST':
            message=request.POST.get('message','')
            data=models.messages(sender=request.session['username'],reciever=res,message=message)
            data.save()
        messages=models.messages.objects.filter(Q(sender=request.session['username'],reciever=res)| Q(sender=res,reciever=request.session['username'])).order_by('date_time')
        return render(request,"chat/chat.html",{'status':True,'data':messages})
    return redirect('login:login_User')