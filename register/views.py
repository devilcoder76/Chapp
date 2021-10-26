from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
# Create your views here.
def register(request):
    if request.session.has_key('username'):
        return HttpResponse("Logout First")
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        pro_image=request.FILES.get('pro_image','')
        data=models.UserData(fname=fname,lname=lname,username=username,password=password,pro_image=pro_image)
        data.save()
        return redirect("login:login_User")
    else:
        return render(request,"register/register.html")