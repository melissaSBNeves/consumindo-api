from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import HolidayForm
from .serializer import HolidaySerializer
from .models import Holiday
from django.contrib.auth.decorators import login_required

import requests;

@api_view(['GET'])
def search_year(request):
     form = HolidayForm()
     return render (request, 'index.html', {'form': form})


@api_view(['GET']) #DEFINIR QUE SÓ ACEITA O MÉTODO GET
def get_holiday(request):

    if request.method == 'GET':

        try:
            if request.GET['ano']:

                ano = request.GET['ano']

                try:
                    url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
                    reponse = requests.get(url)
                    data = reponse.json()
                    form = HolidayForm()
                    return render (request, 'index.html', {'data': data, 'form': form})
                
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
            else:
                 return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url="/auth/login/")
@api_view(['GET', 'POST'])
def save_holiday(request):
     
     if request.method == 'POST':
        
           current_user = request.user

           nome= request.POST["name"]
           data= str(request.POST["data"])
           tipo = request.POST["tipo"]
    

           data_dict = [{
                'date': data,
                'name': nome,
                'type': tipo,
                'user': current_user.id
           }]
           

           for i in range (0,len(data_dict)):
            serializer = HolidaySerializer(data=data_dict[i])

            check_holiday = Holiday.objects.filter(date=data)
            check_user = Holiday.objects.filter(user_id=current_user.id)
        


            if check_holiday and check_user:
                 return HttpResponse("Essa data já foi registrada")
            
            else:
                if serializer.is_valid():
                    serializer.save()
                    return render (request, 'created.html')
  
     Response(status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url="/auth/login/")
@api_view(['GET'])
def holiday_list(request):

    if request.method == 'GET':
        try:      
           current_user = request.user

           try:
                data = Holiday.objects.all().filter(user_id=current_user.id)
                # serializer = HolidaySerializer(data)

                return render (request, 'home.html', {'data': data, 'nome': current_user.first_name})

           except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@login_required(login_url="/auth/login/")
@api_view(['DELETE', 'GET'])
def holiday_delete(request, pk):

    if request.method == 'GET':
          try:
                data = Holiday.objects.filter(pk=pk)
                data.delete()


                return render (request, 'delete.html')
          except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse("Via get")
           
       