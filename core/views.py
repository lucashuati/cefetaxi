from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from forms import LoginForm, NovoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from models import *

def index(request):
    if request.user.is_authenticated():
        motorista = Motorista.objects.filter(django_user=request.user)
        associado = Associado.objects.filter(django_user=request.user)
        if motorista.count() > 0:
            return render(request, 'cefetaxi/motorista.html', {'motorista': motorista[0]})
        elif associado.count() > 0:
            return render(request, 'cefetaxi/associado.html', {'associado': associado[0]})
        else:
            return redirect('/admin/')

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = request.POST['user']
            password = request.POST['password']

            user = authenticate(username=user, password=password)

            if user is not None:
                motorista = Motorista.objects.filter(django_user=user)
                associado = Associado.objects.filter(django_user=user)
                login(request, user)
                if motorista.count() > 0:
                    return render(request,'cefetaxi/motorista.html',{'motorista': motorista[0]})
                elif associado.count() > 0:
                    return render(request, 'cefetaxi/associado.html', {'associado': associado[0]})
                else:
                    return redirect('/admin/')
            else:
                return HttpResponse("<h1>ERRO</h1><a href='/';>Voltar</a>")
    else:
        form = LoginForm()

    return render(request, 'cefetaxi/index.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')

def new_user(request):
    if request.user.is_authenticated():
        redirect('/')
    elif request.method == 'POST':
        form = NovoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nome']
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['senha']
            type = form.cleaned_data['tipo']
            email = form.cleaned_data['email']
            name_error = User.objects.filter(username=user_name)
            email_error = User.objects.filter(email=email)

            if(name_error.count() > 0 or email_error.count() > 0):
                return HttpResponse("<p>ERRO</p>")
            else:
                user = User.objects.create_user(username=user_name,email=email,password=password,first_name=name)
                user.save()
                if(type == 'motorista'):
                    motorista = Motorista(django_user=user)
                    motorista.save()
                else:
                    associado = Associado(django_user=user)
                    associado.save()
                return redirect('index')
    else:
        form = NovoForm()

    return render(request,'cefetaxi/novo.html', {'form': form})

