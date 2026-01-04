from django.contrib import admin
from django.urls import path, include 
from home import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logoutuser,name="logout"),


]
