from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import FireAlert
from .serializers import FireAlertSerializer
import pyrebase

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


class FireAlertApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = db.child("dataset").get().val()
        # data = FireAlert.objects.filter(user=request.user.id)
        serializer = FireAlertSerializer(data, many=True)
        return Response(data, status=200)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'img': request.data.get('img'),
            'isFire': request.data.get('isFire'),
            'user': request.user.id
        }
        res = db.child("dataset").push(data)
        # serializer = FireAlertSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=201)

        return Response(res, status=201)
