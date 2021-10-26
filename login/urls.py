from django.urls import path
from . import views
app_name="login"

urlpatterns=[
    path('login/',views.login,name="login_User"),
    path('profile/',views.view_profile,name="profile_User"),
    path('profile/<int:pk>',views.profile,name="profile"),
    path('logout/',views.logout,name="logout_User"),
    path('users/',views.people,name="people"),
    path('users/<int:pk>',views.add_friend,name="add_friend"),
    path('friends/',views.view_friend,name="friend_User"),
    

]