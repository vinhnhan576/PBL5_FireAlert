from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import FireAlert, Image
from .serializers import FireAlertSerializer
import pyrebase
import requests as r
import json
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen

from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

config = {
    "apiKey": "AIzaSyBncKfVp7uLOE9n2oILjPl25R1CCUvAZzQ",
    "authDomain": "fire-alert-b50c7.firebaseapp.com",
    "projectId": "fire-alert-b50c7",
    "storageBucket": "fire-alert-b50c7.appspot.com",
    "messagingSenderId": "432406844643",
    "appId": "1:432406844643:web:d6239f33ca54ce7b69e1d6",
    "measurementId": "G-0LGLKPLFSB",
    "databaseURL": "https://fire-alert-b50c7-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

class FireAlertApiView(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = db.child("dataset").get().val()
        # data = FireAlert.objects.filter(user=request.user.id)
        serializer = FireAlertSerializer(data, many=True)
        return Response(data, status=200)
    
class FireAlertExpoTokenApiView(APIView):
     #permission_classes = [permissions.IsAuthenticated]

     def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'expo_token': request.data.get('expo_token'),
        }
        res = db.child("expo_token").push(data)
        return Response(res, status=201)
     

     def get(self, request, *args, **kwargs):
        expo_token_db = db.child("expo_token").get().val()
        expo_token = []
        for i in expo_token_db.values():
            expo_token.append(i['expo_token'])
        if expo_token == []:
            return Response(status=404)
        print(expo_token)
        message = {
        'to' : expo_token,
        'title' : 'Fire Alert',
        'body' : 'Fireeeeeee'
        }
        r.post('https://exp.host/--/api/v2/push/send', json=message)
        return Response(message, status=200)
     
@parser_classes((MultiPartParser, ))
class FireAlertImageApiView(APIView):
    def post(self, request, *args, **kwargs):
        image = request.FILES["image"]
        print(image)
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'
        image.name = name
        db.child("image").push(name)
        storage.child(name).put(image)
        return Response("Upload image to firebase successfully", status=200)