from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_passwords, is_password_usable, check_password

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from datetime import datetime

# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def check_login(request):
    if not request.body:
        return HttpResonse(status=400)
    elif request.method = 'GET':
        data = JSONParser.parse(request)
        try:
            user = Users(username=data['username'], password=data['password'])
        except:
            return HttpResponse(status=400)
        if not user:
            return HttpResponse(status=400)
        return HttpResponse(status=202)
    else:
        return HttpResponse(status=404)

def notify_parent(request):
    if not request.body:
        return HttpResponse(status=400)
    elif request.method = 'GET':
        data = JSONParser.parse(request)
        try:
            users = 
        except:
            return HttpResponse(status=400)
        if not user:
            return HttpReponse(status=400)
        return HttpResponse(status=202)
    else:
        return HttpResponse(status=404)
