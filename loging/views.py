from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .forms import PublicarForm
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.



def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
                
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'La contraseña no coincide'
        })

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html',{'productos': productos}) 

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña no es correcto'
            })
        else:
            login(request,user)
            return redirect('/')

def publicacion(request):
    if request.method == 'GET':
        return render(request, 'publicar.html',{
        'form': PublicarForm
    })
    else:
        try:
            form = PublicarForm(request.POST)
            new_publicacion = form.save(commit=False)
            new_publicacion.user = request.user
            new_publicacion.save()
            return redirect('home')
        except ValueError:
            if request.method == 'GET':
                return render(request, 'publicar.html',{
                'form': PublicarForm, 
                'error': 'Datos mal ingresados'
            })

@login_required
def mispublis(request):
    productos = Producto.objects.filter(user=request.user)
    return render(request, 'mispublis.html',{'productos': productos}) 

@login_required
def editarpubli(request,id):
    producto = Producto.objects.get(id = id)
    if request.method == 'GET':
        form = PublicarForm(instance=producto)
        contexto = {
            'form':form
        }
    else:
        form = PublicarForm(request.POST, instance = producto)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mispublis')
    return render(request, 'detallepublicacion.html',contexto)    

@login_required
def eliminarpubli(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('mispublis')








# quede en el min 2:17:15 https://www.youtube.com/watch?v=e6PkGDH4wWA&ab_channel=Fazt
