from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
import json 

def get_user_permissions(request):
    print request.GET.get(request)
    return HttpResponse(json.dumps(str({"1":"1"})))
