from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
# Create your views here.


def upload(request):
    if request.session.has_key('username'):
        if request.method=="POST":
            image=request.FILES.get('feed_img','')
            caption=request.POST.get('feed_caption','')
            data=models.feed_image(user_id=request.session['id'],username=request.session['username'],image=image,caption=caption,likes=0,comments=0)
            data.save()
            return redirect("login:profile_User")
        return render(request,'newsfeed/upload.html',{'status':True})
    return redirect('login:login_User')

def view_feed(request):
    if request.session.has_key('username'):
        data=models.feed_image.objects.all().order_by('-date_time')
        if data:
            return render(request,"newsfeed/feed.html",{'status':True,'data':data})
        return render(request,"newsfeed/feed.html",{'status':True,'message':"Nothing to show: :("})
        
    return redirect('login:login_User')

def like(request,pk):
    if request.session.has_key('username'):
        img_data=models.feed_image.objects.get(id=pk)
        try:
            user_data=models.likes.objects.get(user_id=request.session['id'],img_id=pk)
        except models.likes.DoesNotExist:
            data=models.likes(user_id=request.session['id'],username=request.session['username'],liked_username=img_data.username,img_id=pk)
            img_data.likes+=1
            data.save()
            img_data.save()
        return redirect('newsfeed:feed_User')
    return redirect('login:login_User')

def dislike(request,pk):
    if request.session.has_key('username'):
        img_data=models.feed_image.objects.get(id=pk)
        try:
            user_data=models.likes.objects.get(user_id=request.session['id'],liked_username=img_data.username,img_id=pk)
            img_data.likes-=1
            user_data.delete()
            img_data.save()
            print('Done')
        except models.likes.DoesNotExist:
            pass
        return redirect('newsfeed:feed_User')
    return redirect('login:login_User')

def comment(request,pk):
    if request.session.has_key('username'):
        img_data=models.feed_image.objects.get(id=pk)
        if request.method=='POST':
            comment=request.POST.get('comment','')
            data_ob=models.comments(user_id=request.session['id'],username=request.session['username'],cmt_username=img_data.username,img_id=pk,comment=comment)
            data_ob.save()
        try:
            data=models.comments.objects.filter(img_id=pk)
        except models.comments.DoesNotExist:
            data=None
        img_url=models.feed_image.objects.get(id=pk).image.url
        return render(request,"newsfeed/comments.html",{'img_url':img_url,'data':data,'status':True})
    
    return redirect('login:login_User')
