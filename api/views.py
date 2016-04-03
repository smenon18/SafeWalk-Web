from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.hashers import make_passwords, is_password_usable, check_password
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.models import User, ParentalRel, InTransit
from api.serializers import UserSerializer, ParentalRelSerializer, InTransitSerializer

from datetime import datetime

# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def check_login(request):
    if not request.body:
        return HttpResponse('{"error": "Empty request data"}', status=400, content_type="application/json")
    elif request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            user = User.objects.filter(password=data['password'], email=data['email'])
        except:
            return HttpResponse('{"error": "Invalid request data"}', status=400, content_type="application/json")
        if not user:
            return HttpResponse('{"error": "No user exists"}', status=400, content_type="application/json")
        return HttpResponse(status=202)
    else:
        return HttpResponse('{"error": "Invalid methods"}', status=404, content_type="applicaiton/json")

def notify_parent(request):
    if not request.body:
        return HttpResponse(status=400)
    elif request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            user = User(email=data['email'], password=data['password'])
            parents = ParentalRel.objects.all().filter(child=user)
        except:
            return HttpResponse(status=400)
        if not parents:
            return HttpReponse(status=400)
        # Figure out what calculations are necessary
        for p in parents:
            htmlMessage = "Hi " + p.get_email() + ",<br><br> " + "Your Child is on the move.<br><br> Thank You, SafeWalk"
            try:
                send_mail("Your Child is on the move.", "", settings.EMAIL_HOST_USER, p.get_parent().get_email(), fail_silently=False, html_message=htmlMessage)
            except:
                return HttpResponse(status=417) # Expectation Failed
        return HttpResponse(status=202)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def create_user(request):
    if not request.body:
        return HttpResponse(status=404)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User()
            validate_email(data['email'])
        except ValidationError:
            return HttpResponse(status=400)
        users = User.objects.all()
        if not users:
            serializer = UserSerializer(user,data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(status =202) #First User
            return HttpResponse(status=400)
        else:
            for u in users:
                if data['email'] == u.get_email():
                    return HttpResponse(status=400)
            serializer = UserSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(status=202)
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def request_parent(request):
    if not request.body:
        return HttpResponse(status=404)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            requesting_user = User.objects.get(data['requesting_email'])
            requested_user = User.objects.get(email=data['requested_email'])
            htmlMessage = "Hi " + requested_user.get_email() + ",<br><br> " + requesting_user.get_email() + "is requesting to connect with you.<br>To confirm this connection <a href='safewalk-web.herokuapp.com/confirm?parent=" + requesting_user.get_email() + "&child=" + requested_user.get_email() + ">please click here.</a>'<br><br> Thank You, SafeWalk"
            send_mail("Request", "", settings.EMAIL_HOST_USER, requested_user.get_email(), fail_silently=False,html_message=htmlMessage)
        except:
            return HttpResponse(status=400)
        return HttpResponse(status=202)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def confirm_relation(request):
    if not request.body:
        return HttpResponse(status=404)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            parent = User(email=data['parent'])
            child = User(email=data['child'])
        except:
            return HttpResponse(status=400)
        relations = ParentalRel.objets.all();
	if not relations:
            serializer = ParentalRelSerializer(child, parent)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(status =202) #First User
            return HttpResponse(status=400)
        else:
            for r in relations:
                if data['parent'] == r.parent.get_email() and data['child'] == r.parent.get_email():
                    return HttpResponse(status=400)
            serializer = ParentalRelSerializer(child, parent)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(status=202)
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=404)

def list_users(request):
    if request.method == 'GET':
        users = User.Objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)
    
