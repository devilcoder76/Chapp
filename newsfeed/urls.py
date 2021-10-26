from django.urls import path
from . import views
app_name="newsfeed"

urlpatterns =[
    path('upload/',views.upload,name="upload_User"),
    path('feed/',views.view_feed,name="feed_User"),
    path('like/<int:pk>',views.like,name="like_User"),
    path('dislike/<int:pk>',views.dislike,name="dislike_User"),
    path('comment/<int:pk>',views.comment,name="comment_User")
]