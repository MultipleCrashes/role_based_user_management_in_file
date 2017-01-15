from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
import json 

def get_user_permissions_list(request):
    response = {"res_str":"","res_code":0}
    user = ''
    try:
        user=request.POST.get('user')
        if user is None:
            response['res_str'] ="Mandatory param missing"
    except Exception as e:
            response['res_str']=str(e)
    return HttpResponse(json.dumps(response))
