from django.test import TestCase
from usermanager.models import *
# Create your tests here.
import requests 
import unittest 
import json 

API_SERVER = 'http://127.0.0.1:8000/'

class UserManagerTestCase(TestCase):
    
    def setUp(self):
        pass 

    def test_user_api_status_code(self,user='user1'):
        print "Api url",API_SERVER+'usermanager/user/?user='+user
        try:
            print "Sending get request -> ",API_SERVER+'usermanager/user/?user='+user
            user_permissions_name = requests.get(API_SERVER+'usermanager/user/?user='+user)
        except Exception as e:
            print "Exception found while hitting get api->",str(e)
        print "Status code of get request-> ",user_permissions_name.status_code
        print "Expected status code :    ->  200 "
        self.assertEqual(user_permissions_name.status_code,200)
        print "="*20

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
        print "="*20
