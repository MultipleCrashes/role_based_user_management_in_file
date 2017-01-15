from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
import os 
pwd = '/home/biswajit/user_management_project/user_management/user_management/usermanager/'
print "pwd ",pwd
import json 

user_file_name = 'userapp.txt'

def get_user_permissions_list(request):
    response = {"res_str":"","res_code":200}
    user = ''
    try:
        user=request.POST.get('user')
        if user is None:
            response['res_str'] ="Mandatory param missing"
            response['res_code']=400
            return HttpResonse(reponse)
    except Exception as e:
            response['res_str']=str(e)
    all_roles = get_key_value(user,'roles') # List
    permission_list = []
    for roles in all_roles:
        perms = get_key_value(roles,'permissions')
        permission_list = permission_list + perms
    perm_name = []
    for permission in permission_list:
        permission_name = get_key_value(permission,'name')
        perm_name = perm_name + [permission_name]
    response['res_str']=perm_name
    return HttpResponse(json.dumps(response))

def get_key_value(identifier,return_field):
    with open(pwd+user_file_name,'r+b') as userfile:
        for lines in userfile:
            lines=lines.rstrip("\n") 
            lines_json =eval(json.loads(lines))
            if lines_json['id'] == identifier:
                all_values = lines_json[return_field]
    return all_values

    
