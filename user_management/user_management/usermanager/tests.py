from django.test import TestCase
from usermanager.models import *
# Create your tests here.
import requests 
import unittest 
import json 


API_SERVER = 'http://127.0.0.1:8000/'

class UserManagerTestCase(TestCase):
    
    def setUp(self):
        print "\n"+"="*20
        pass 

    def test_user_api_status_code(self,user='user1'):
        print "Api url",API_SERVER+'usermanager/user/?user='+user
        print "Sending get request -> ",API_SERVER+'usermanager/user/?user='+user
        try:
            user_permissions_name = requests.get(API_SERVER+'usermanager/user/?user='+user)
        except Exception as e:
            print "Exception found while hitting get api->",str(e)
        print "Status code of get request-> ",user_permissions_name.status_code
        print "Expected status code :    ->  200 "
        self.assertEqual(user_permissions_name.status_code,200)


    def test_user_api_response_str(self,user='user1'):
        print "Sending get request -> ",API_SERVER+'usermanager/user/?user='+user
        try:
            user_permissions_name = requests.get(API_SERVER+'usermanager/user/?user='+user)
        except Exception as e:
            print "Exception found while hitting get api->",str(e)
        res = json.loads(user_permissions_name.text)
        #response string validation
        print "Response for get request  ->",user_permissions_name.text
        print "Expected response text     -> {\"res_str\": [\"Can check balance\", \"Can deposit\", \"Can Transfer\", \"Can withdraw\"], \"res_code\": 200}"
        self.assertEquals(str(res['res_str']),str([u'Can check balance', u'Can deposit', u'Can Transfer', u'Can withdraw']))


class PermissionTestCase(TestCase):
    
    def setUp(self):
        print "\n"+"="*20
        pass 

    def test_permission_check_status_code_correct_perm(self,user='user1',perm='perm5'):
        api_uri = API_SERVER+ 'usermanager/checkpermission/?user='+user+'&permission='+perm
        res =''
        print "Sending get request" ,api_uri
        print "API URL",api_uri
        try:
            res = requests.get(api_uri)
        except Exception as e:
            print "Exception found while executing get query",str(e)
        print "Response status code -> ",res.status_code
        print "Expected status code -> 200",
        self.assertEquals(res.status_code,200)


    def test_permission_check_status_code_no_perm(self,user='user1',perm='perm500'):
        api_uri = API_SERVER+ 'usermanager/checkpermission/?user='+user+'&permission='+perm
        res =''
        try:
            res = requests.get(api_uri)
        except Exception as e:
            print "Exception found while executing get query",str(e)  
        print "Response status code -> ",res.status_code
        print "Expected status code -> 200",
        self.assertEquals(res.status_code,200)
        

    def test_check_res_string_correct_perm(self,user='user1',perm='perm5'):
        api_uri = API_SERVER+ 'usermanager/checkpermission/?user='+user+'&permission='+perm
        res =''
        try:
            res = requests.get(api_uri)
        except Exception as e:
            print "Exception found while executing get query",str(e)
        res = json.loads(res.text)
        print "Expected response string {u'res_str': True, u'res_code': 200}"
        print "Got response string  -> ",res
        self.assertEquals(res['res_str'],True)    
        


    def test_check_res_string_wrong_perm(self,user='user1',perm='perm50'):
        api_uri = API_SERVER+ 'usermanager/checkpermission/?user='+user+'&permission='+perm
        res =''
        try:
            res = requests.get(api_uri)
        except Exception as e:
            print "Exception found while executing get query",str(e)
        res = json.loads(res.text)
        print "Expected response string {u'res_str': False, u'res_code': 200}"
        print "Got response string  -> ",res
        self.assertEquals(res['res_str'],False)    
        

        
class RolesTestCase(TestCase):
    
    def setUp(self):
        print "\n"+"="*20
        pass         


    def test_roles_response_str(self,role='role1',permission='perm4'):
        api_uri = API_SERVER+ 'usermanager/roles/'
        res =''
        try:
            res = requests.post(api_uri,data={"role":role,"permission":"perm4"})
        except Exception as e:
            print "Exception found while executing get query",str(e)
        res = json.loads(res.text)
        #print "Expected response string {"res_str": ["perm4"], "res_code": 200}"
        print "Got response string  -> ",res
        self.assertEquals(str(res['res_str']),str([u'perm4']))

    def test_roles_response_code(self,role='role1',permission='perm4'):
        api_uri = API_SERVER+ 'usermanager/roles/'
        res =''
        try:
            res = requests.post(api_uri,data={"role":role,"permission":"perm4"})
        except Exception as e:
            print "Exception found while executing get query",str(e)
        res = json.loads(res.text)
        #print "Expected response string {"res_str": ["perm4"], "res_code": 200}"
        print "Got response string  -> ",res
        self.assertEquals(res['res_code'],200)
