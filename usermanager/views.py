from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
import os 
import shutil
user_file_name = 'userapp.txt'
DATA_FILE_DIR = os.path.dirname(os.path.abspath('__file__')) 
DATA_FILE = DATA_FILE_DIR + os.sep + 'usermanager' + os.sep + user_file_name
import json 


def get_user_permissions_list(request):
    response = {"res_str":"","res_code":200}
    user = ''
    if not request.method=='GET':
        response['res_str']='Method not allowed'
        response['res_code'] = 405 
        return HttpResponse(json.dumps(response))
    try:
        user=request.GET.get('user')
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
    all_values =''
    with open(DATA_FILE,'r+b') as userfile:
        for lines in userfile:
            lines=lines.rstrip("\n") 
            lines_json =eval(json.loads(lines))
            if lines_json['id'] == identifier:
                all_values = lines_json[return_field]
    return all_values

def get_entitled(request):
    '''If perm id is found in any of user chain then True else false'''
    response ={"res_str":"","res_code":200}
    user = ''
    if not request.method=='GET':
        response['res_str']='Method not allowed'
        response['res_code'] = 405
        return HttpResponse(json.dumps(response))
    try:
        user = request.GET.get('user')
        permissions = request.GET.get('permission')
        if user==None or permissions==None:
            response['res_str']="Missing mandatory parameter"
            return HttpResponse(json.dumps(response))
        print "Permission",permissions
    except Exception as e:
        print "Exception found while getting request params",str(e)
    all_roles = get_key_value(user,'roles') # List
    permission_list = []
    for roles in all_roles:
        perms = get_key_value(roles,'permissions')
        permission_list = permission_list + perms
        perm_name = []
        print "list",permission_list
        for permission in permission_list:
            permission_name = get_key_value(permission,'name')
            perm_name = perm_name + [permission_name]
            response['res_str']=perm_name
            print "permissions -> ",permissions
            if permissions in permission:
                print "User is permitted for the action",permissions
                response['res_str'] = True 
                return HttpResponse(json.dumps(response))
    response['res_str']= False
    return HttpResponse(json.dumps(response))        


def modify_permission(request):
    response = {"res_str":"","res_code":200}
    role = ''
    permission = ''
    if not request.method=='POST':
        response['res_str']='Method not allowed'
        response['res_code'] = 405
        return HttpResponse(json.dumps(response))
    try:
        role = request.POST.get('role')
        permission = request.POST.get('permission').split(',')
        permission = [str(x) for x in permission] # convert to list without unicode
        new_permission=''
        if role==None or permission==None:
            response['res_str']='Mandatory parameter missing'
    except Exception as e:
        print "Exception found while getting values in request",str(e)
        response['res_str'] = str(e) 
        response['res_code'] = 400
    with open(DATA_FILE+'temp','w') as newfile:
        with open(DATA_FILE,'r+') as userfile:
            for lines in userfile:
                lines=lines.rstrip("\n")
                lines_json =eval(json.loads(lines))
                if lines_json['id']==role:
                    print "lines",lines_json
                    lines_json['permissions']=permission
                    new_permission = lines_json['permissions']
                    print "new line",lines_json
                    newfile.write(json.dumps(str(lines_json))+"\n")
                else:
                    newfile.write(str(lines)+"\n")
        os.remove(DATA_FILE)
        os.rename(str(DATA_FILE+'temp'),DATA_FILE)
    response['res_str'] = new_permission         
    return HttpResponse(json.dumps(response))


def delete_permission(request):
    response = {"res_str":"","res_code":200}
    role = ''
    permission = ''
    new_permission = ''
    if not request.method=='POST':
        response['res_str']='Method not allowed'
        response['res_code'] = 405 
        return HttpResponse(json.dumps(response))
    try:
        role = request.POST.get('role')
        permission = request.POST.get('permission').split(',')
        permission = [str(x) for x in permission]
        print "permission",permission
        if (role==None) or (permission==None):
            response['res_str']='Mandatory parameter missing'
    except Exception as e:
        print "Exception found while getting values in request",str(e)
        response['res_str'] = str(e) 
        response['res_code'] = 400
    with open(DATA_FILE+'temp','w') as newfile:
        with open(DATA_FILE,'r+') as userfile:
            for lines in userfile:
                lines=lines.rstrip("\n")
                lines_json =eval(json.loads(lines))
                if lines_json['id']==role:
                    try:
                        print "Taking diff of ",set(lines_json['permissions']) - set(permission)
                        lines_json['permissions']=list(set(lines_json['permissions']) -set(permission))
                    except Exception as e:
                        response['res_str'] = str(e)
                    new_permission = lines_json['permissions']
                    print "new line",lines_json
                    newfile.write(json.dumps(str(lines_json))+"\n")
                else:
                    newfile.write(str(lines)+"\n")
        os.remove(DATA_FILE)
        os.rename(str(DATA_FILE+'temp'),DATA_FILE)
    response['res_str'] = "new_permission:"+str(new_permission)      
    return HttpResponse(json.dumps(response))


