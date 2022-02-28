from tkinter.tix import Tree
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Safepoints
from .serializers import userSerializer, safePointSerializer

# Create your views here.
class user(APIView):

    def get(self,request):
        user_id = request.data['id']
        user  = User.objects.get(id=user_id)
        serializer = userSerializer(user)
        return Response(serializer.data)

    def post(self,request):
        pass


class fetchSafepoint(APIView):

    def get(self,request):
        sp = Safepoints.objects.all()
        serializer = safePointSerializer(sp,many=True)
        return Response(serializer.data)