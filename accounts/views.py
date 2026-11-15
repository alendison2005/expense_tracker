from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from accounts.serializers import Userserializer


class Signupview(APIView):
    def post(self,request):
        form_data= request.data
        serializer_instance = Userserializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)