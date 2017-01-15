from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
import os 
pwd = '/home/biswajit/user_management_project/user_management/user_management/usermanager/'
print "pwd ",pwd
import json 

user_file_name = 'userapp.txt'

def get_user_permissions_list(request):
    response = {"res_str":"","res_code":0}
    user = ''
    try:
        user=request.POST.get('user')
        if user is None:
            response['res_str'] ="Mandatory param missing"
    except Exception as e:
            response['res_str']=str(e)
    with open(pwd+user_file_name,'r+b') as userfile:
        for lines in userfile:
            lines = json.loads(lines)
            print lines
    return HttpResponse(json.dumps(response))
