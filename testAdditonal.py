
import unittest
import os
import testLib


class TestAdd(testLib.RestTestCase):
    def testEmptyUser(self):
        response = self.makeRequest("/users/add", method = 'POST', data = {'user':'', 'password' : '123'})
        self.assertTrue('errCode' in response)
        
        self.assertResponse(response, count= -1, errCode = TestAdd.ERR_BAD_USERNAME)

    def testLongUser(self):
        name = "1"*200
        respData = self.makeRequest("/users/add", method = 'POST', data = {'user': name, 'password' : '123'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, count= -1, errCode = TestAdd.ERR_BAD_USERNAME)
        
    def testLValidOne(self):
        respData = self.makeRequest("/users/add", method = 'POST', data = {'user':'justTest', 'password' : 'noMore'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, count = 1, errCode = TestAddUser.SUCCESS)



class TestLogin(testLib.RestTestCase):

    def testBadLogin(self):
        
        respData = self.makeRequest("/users/login", method = 'POST', data = {'user':'testLogin', 'password' : 'notExist'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, count = -1, errCode = TestLogin.ERR_USER_EXISTS)
      
