from django.urls import path
from . import views 

urlpatterns = [
 path('', views.index, name='index'),
 path('signup',views.signup,name='signup'),
 path('login',views.loginpage,name='login'),
 path('logoutuser',views.logoutuser,name='logoutuser'),
 path('dashboard',views.dashboard,name= 'dashboard'),
 path('periodt',views.periodt,name= 'periodt')


]