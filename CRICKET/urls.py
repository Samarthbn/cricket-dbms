"""CRICKET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRICKET_APP.views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('teamsearch/', teamsearch),
    path('matchsearch/', matchsearch),
    path('playersearch/', playersearch),
    path('report/', report),
    path('userlogin/', userlogin),
    path('dashboard/', dashboard),
    path('matchdata/', matchdata),
    path('deletematch/', deletematch),
    path('matchdetails/', matchdetails),
    path('teamdetails/', teamdetails),

    path('matchin/', matchin),
    path('alo/', alo),
    path('dashboar/', dashboar),
    path('report1/', report1),
    path('teamin/', teamin),
    path('captaindetails/', captaindetails),
    path('captaindetails/', captaindetails),
    path('playerdata/', playerdata),
    path('umpiredata/', umpiredata),

    path('datac/', datac),
    path('datam/', datam),
    path('datap/', datap),
    path('datau/', datau),






    path('delt/', delt),















    path('signup/', signup),
    path('sg/', sg),
    path('lo/', lo),
    path('searchs/', searchs),
    path('searchm/', searchm),
    path('searchp/', searchp),


    path('data/', data),
    path('dataf/', dataf),
    
    # path('report/',report),





]
