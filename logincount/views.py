from django.shortcuts import get_object_or_404, render
from logincount.UsersModel import UsersModel
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
import json
##from loginincoun.UsersModel import UsersModel
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
import unittest
import logincount.tests as tests

@csrf_exempt
def add(request):
	if request.method == 'POST': ## if it is Json.
		if request.META['CONTENT_TYPE'] != 'application/json':
			return index(request)
		dataGot = json.loads(request.body)
		if ('user' not in dataGot) or ('password' not in dataGot):
			return index(request)
		dataUser = UsersModel()
		response = dataUser.add(dataGot['user'], dataGot['password'])
		if response[0] == UsersModel.SUCCESS:
			get = json.dumps({'errCode':response[0], 'count':response[1]})
			return HttpResponse(get, content_type = 'application/json') 
		get = json.dumps({'errCode':response[0]})
		return HttpResponse(get, content_type = 'application/json')
	return index(request)

@csrf_exempt
def login(request):
	if request.method =='POST':
		if request.META['CONTENT_TYPE'] != 'application/json':
			return index(request)
		dataGot = json.loads(request.body)
		if ('user' not in dataGot) or ('password' not in dataGot):
			return index(request)
		dataUser = UsersModel()
		response = dataUser.login(dataGot['user'],dataGot['password'])
		if response[0] == UsersModel.SUCCESS:
			get = json.dumps({'errCode' : response[0], 'count' : response[1]})
			return HttpResponse(get, content_type = 'application/json')
		get = json.dumps({'errCode' : response[0]})
        return HttpResponse(get, content_type = 'application/json')
	return index(request)


@csrf_exempt
def reset(request):
	if request.method =='POST':
		if request.META['CONTENT_TYPE'] != 'application/json':
			return index(request)
		dataUser = UsersModel()
		response = dataUser.TESTAPI_resetFixture()
		if response == UsersModel.SUCCESS:
			get = json.dumps({'errCode':response})
			return HttpResponse(get, content_type = 'application/json' )
	return index(resqest)


"""
@csrf_exempt
def unit(request):
    if request.method == 'POST':
		if request.META['CONTENT_TYPE'] != 'application/json':
			return index(request)
		loadModule = unittest.TestLoader().loadTestsFromModule(testUnit)
		fileToWrite = open("log", "w")
		runTheTest = unittest.TextTestRunner(stream = fileToWrite)
		result = runTheTest.run(fileToWrite)
		sumError = len(result.failures) + len(result.errors)
		total = result.testsRun
		fileToWrite.close()

		fileToRead = open("log", "r")
		get = json.dumps({'nrFailed' : sumError, 'output' : fileToRead.read(), 'totalTests' : total})
		fileToRead.close()
		return HttpResponse(get, content_type = 'application/json' )
	#return index(request)
"""
def index(request):
    
  return render(request, 'logincount/client.html', {})





# Create your views here.
