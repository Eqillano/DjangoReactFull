from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


User = get_user_model()


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({"error":"Already exists"})
            else:
                if len(password) < 6:
                   return Response({'error':'too short'})
                else:
                    user = User.objects.create_user(email=emmail,password=password,name=name)
                    user.save()
                    return Response({"success":"well dones"})
        else:
            return Response({"error":'Ps do not match'})
