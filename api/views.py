from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.hashers import make_passwords, is_password_usable, check_password
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.models import User, ParentalRel
from api.serializers import UserSerializer, ParentalRelSerializer

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
    elif request.method == 'GET':
        data = JSONParser.parse(request)
        try:
            user = User(username=data['username'], password=data['password'])
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
    elif request.method == 'GET':
        data = JSONParser.parse(request)
        try:
            user = User(username=data['username'], password=data['password'])
            parents = ParentalRel.objects.all().filter(child=user)
        except:
            return HttpResponse(status=400)
        if not parents:
            return HttpReponse(status=400)
        # Figure out what calculations are necessary
        for p in parents:
            htmlMessage = "Hi " + u.get_username() + ",<br><br> " + "Your Child is on the move.<br><br> Thank You, SafeWalk"
            try:
                send_mail("Your Child is on the move.", "", settings.EMAIL_HOST_USER, p.get_parent().get_email(), fail_silently=False, html_message=htmlMessage)
            except:
                return HttpResponse(status=417) # Expectation Failed
        return HttpResponse(status=202)
    else:
        return HttpResponse(status=404)

def create_user(request):
    if not request.body:
        return HttpResponse(status=404)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        try:
            validate_email(data['email'])
        except ValidationError:
            return HttpResponse(status=400)
        users = User.objects.all()
        if not users:
            return HttpResponse(status =202) #First User
        else:
            for u in users:
                if data['email'] == u.get_email() or data['username'] == u.get_username():
                    return HttpResponse(status=400)
            return HttpResponse(status=202)
    else:
        return HttpResponse(status=404)
