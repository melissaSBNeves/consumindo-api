from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from holiday.urls import urlpatterns

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)

        if user:
            return HttpResponse("Já existe um usuário cadastrado com esse email")
        
        new_user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
        new_user.save()

        return render(request, 'login.html')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login_django(request, user)
            return redirect('list-holiday')
        else:
            return HttpResponse("Não logou")
    else:
        return render(request, 'login.html')
    

@login_required(login_url="/auth/login/")
def logout_view(request):
    logout(request)
    return render (request, 'login.html')
