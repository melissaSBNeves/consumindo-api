from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET']) #DEFINIR QUE SÓ ACEITA O MÉTODO GET
def get_user(request):

    if request.method == 'GET':
        users = User.objects.all() #TRAZER TODOS OS OBJETOS DO BANCO

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_id(request, id):

    try:
        user = User.objects.get(pk=id)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:
                
                id = request.GET['user'] 

                try:
                    user = User.objects.get(pk=id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)
                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
#CRIANDO DADOS
    if request.method == 'POST':

        new_user = request.data

        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

#FUNÇÕES BÁSICAS DE DB EM DJANGO

# data = User.objects.get(pk=1) #RETORNA UM OBJETO 

# data = User.objects.filter(user_age=18) #RETORNA UMA QUERYSET

# data = User.objects.exclude(user_age=18) #RETORNA UMA QUERYSET

# data.save()

# data.delete()

