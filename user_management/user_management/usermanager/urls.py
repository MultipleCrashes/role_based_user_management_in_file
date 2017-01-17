"""user_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from usermanager import views
from django.views.decorators.csrf import csrf_exempt 
urlpatterns = [
    url(r'^user/', csrf_exempt(views.get_user_permissions_list),name='getuserperms'),
    url(r'^checkpermission/', csrf_exempt(views.get_entitled),name='getentitled'),
    url(r'^roles/', csrf_exempt(views.modify_permission),name='modifypermission'),
    url(r'^permissions/', csrf_exempt(views.delete_permission),name='modifypermission'),
]
