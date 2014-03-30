from django.views.decorators.csrf import csrf_exempt   ## for protection
from logincount.UsersModel import UsersModel
from django.shortcuts import render
from django.http import HttpResponse
import json
import unittest
import logincount.testUnit as testUnit

@csrf_exempt
def add(request):
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] != 'application/json':
            return index(request)
        content = json.loads(request.body)
        if 'user' not in content or 'password' not in content:
            return index(request)
        dataUser = UsersModel()
        response = dataUser.add(content['user'], content['password'])
        if response[0] == UsersModel.SUCCESS: # success
            outcome = json.dumps({'errCode' : response[0], 'count' : response[1]})
            return HttpResponse(outcome, content_type = 'application/json')
        else: 
            outcome = json.dumps({'errCode' : response[0]})
            return HttpResponse(outcome, content_type = 'application/json')
    return index(request)




@csrf_exempt
def login(request):
    if request.method == 'POST': 
        if request.META['CONTENT_TYPE'] != 'application/json':
            return index(request)
        content = json.loads(request.body)
        if 'user' not in content or 'password' not in content:
            return index(request)
        dataUser = UsersModel()
        response = dataUser.login(content['user'], content['password']) 
            
        if response[0] == UsersModel.SUCCESS: # success
            outcome = json.dumps({'errCode' : response[0], 'count' : response[1]})
            return HttpResponse(outcome, content_type = 'application/json')
        else: 
            outcome = json.dumps({'errCode' : response[0]})
            return HttpResponse(outcome, content_type = 'application/json')
    return index(request)
    
@csrf_exempt
def unit(request):
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] != 'application/json':
            return index(request)
        loadModule = unittest.TestLoader().loadTestsFromModule(testUnit) # load the unit test module
        fileToWrite = open("log", "w") # create a file to write to
        runner = unittest.TextTestRunner(stream = fileToWrite, verbosity = 2) # set up the test runner
        result = runner.run(loadModule) # start the test runner
        sumError = len(result.errors) + len(result.failures)
        total = result.testsRun
        fileToWrite.close()
        fileToRead = open("log", "r") # read back from the file
        outcome = json.dumps({'nrFailed' : sumError, 'output' : fileToRead.read() ,'totalTests' : total})
        fileToRead.close()
        return HttpResponse(outcome, content_type = 'application/json')
    return index(request)


    
    
@csrf_exempt
def reset(request):
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] != 'application/json':
            return index(request)
        content = UsersModel()
        response = content.TESTAPI_resetFixture()   
        if response == UsersModel.SUCCESS:
            outcome = json.dumps({'errCode' : response})
            return HttpResponse(outcome, content_type = 'application/json')
    return index(request)
    
    
def index(request):
    return render(request, 'logincount/client.html', {})