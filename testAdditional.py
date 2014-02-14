
import unittest
import os
import testLib


class TestAdd(testLib.RestTestCase):


    def assertResponse(self, respData, count, errCode):
        expected = {'errCode' : errCode}
        if count >= 1:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
 

    def testEmptyUser(self):
        response = self.makeRequest("/users/add", method = 'POST', data = {'user':'', 'password' : 'first'})
        self.assertTrue('errCode' in response)
        
        self.assertResponse(response, errCode = testLib.RestTestCase.ERR_BAD_USERNAME, count= -1)

    def testLongUser(self):
        name = "1"*200
        respData = self.makeRequest("/users/add", method = 'POST', data = {'user': name, 'password' : 'second'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME, count= -1)
        
    def testValidOne(self):
        respData = self.makeRequest("/users/add", method = 'POST', data = {'user':'justTest', 'password' : 'noMore'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, errCode = testLib.RestTestCase.SUCCESS, count = 1)



class TestLogin(testLib.RestTestCase):
  
    def assertResponse(self, respData, errCode, count):
        expected = {'errCode' : errCode}
        if count >= 1:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
 

    def testBadLogin(self):
        
        respData = self.makeRequest("/users/login", method = 'POST', data = {'user':'nononono', 'password' : 'nonono'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS, count = -1)
      
    def setUp(self):
        super(TestLogin, self).setUp()
        self.makeRequest("/users/add", method = 'POST', data = {'user' : 'goodone', 'password' : 'goodone'})
    
    def testGoodLogin(self):
        
        respData = self.makeRequest("/users/login", method = 'POST', data = {'user':'goodone', 'password' : 'goodone'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, errCode = testLib.RestTestCase.SUCCESS, count = 2)  ### this is the second time.
      

    def testBadLoginWithGoodUserName(self):
        respData = self.makeRequest("/users/login", method = 'POST', data = {'user':'goodone', 'password' : 'wrongone'})
        self.assertTrue('errCode' in respData)
        
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS, count = -1)
    