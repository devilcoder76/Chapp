from django.urls import path
from . import views
app_name="chat"

urlpatterns=[
    path('chat/<str:res>',views.chat,name="chat_User")
]