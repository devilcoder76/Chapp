from django.shortcuts import render,redirect
from django.http import HttpResponse
from register import models as reg_models
from newsfeed import models as img_models
from django.db.models import Q

def login(request):
    if request.session.has_key('username'):
        return HttpResponse("You are already logged in.")
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        data=reg_models.UserData.objects.get(username=username,password=password)
        if data:
            request.session['username']=username
            request.session['id']=data.id
            return redirect("login:profile_User")
        else:
            return HttpResponse("Account does not exist")
    else:
        return render(request,'login/login.html')

def profile(request,pk):
    
    if request.session.has_key('username'):
        data=reg_models.UserData.objects.get(id=pk)
        image=img_models.feed_image.objects.filter(user_id=pk)
        return render(request,'login/profile.html',{'status':True,'data':data,'image':image})
    else:
        return redirect("login:login_User")



def view_profile(request):

    if request.session.has_key('username'):
        data=reg_models.UserData.objects.get(id=request.session['id'])
        image=img_models.feed_image.objects.filter(user_id=request.session['id'])
        return render(request,'login/profile.html',{'status':True,'data':data,'image':image})
    else:
        return redirect("login:login_User")

def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
    return redirect('login:login_User')

def people(request):
    if request.session.has_key('username'):
        data=None
        if request.method=="POST":
            search_item=request.POST.get('search','')
            try:
                data=reg_models.UserData.objects.filter(Q(fname__icontains=search_item)| Q(lname__icontains=search_item))
            except reg_models.UserData.DoesNotExist:
                data=None
        return render(request,"login/people.html",{"user":request.session['username'],'status':True,"data":data})
        
    return redirect('login:login_User')

def add_friend(request,pk):
    if request.session.has_key('username'):
        friend=reg_models.UserData.objects.get(id=pk)
        try:
            friend_check=reg_models.Friendslist.objects.get(username=request.session['username'],friend=friend.username)
        except reg_models.Friendslist.DoesNotExist:
            friend_check=None
        if friend_check:
            return redirect('login:people')
        friend_obj=reg_models.Friendslist(user_id=request.session['id'],username=request.session['username'],friend=friend.username,friend_id=pk)
        friend_obj.save()
        return redirect('login:people')        
    return redirect('login:login_User')

def view_friend(request):
    if request.session.has_key('username'):
        print(request.session['id'])
        data_user=reg_models.Friendslist.objects.filter(username=request.session['username'])
        if not data_user:
            return render(request,"login/friends.html",{'status':True,'message':"No friends yet."}) 
        data=[]
        for i in data_user:
            pro=reg_models.UserData.objects.get(username=i.friend)
            data.append({'id':pro.id,'fname':pro.fname,'lname':pro.lname,'username':pro.username})
        return render(request,"login/friends.html",{'status':True,'data':data})
    return redirect('login:login_User')

