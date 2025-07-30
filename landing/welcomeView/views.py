from django.shortcuts import render, redirect
# autenticación del login
from django.contrib.auth import login as lgin
from django.contrib.auth import logout as lgout
from django.contrib.auth import authenticate  # para autenticar usuarios
from django.contrib import messages as msg
# formularios
from .forms import Registro
from django.contrib.auth.models import User
# Products del modelo de la aplicacion products
from products.models import Product
# from django.http import HttpResponse


def index(request):
    """
    Render the welcome page.
    """
    # importar todos los productos del modelo
    products = Product.objects.all()
    # podemos incluir variables en el contexto
    return render(request, 'index.html', {
        'products': products,
    })


def login(request):
    """
    Render the login page.
    """

    if request.user.is_authenticated:
        msg.info(request, "No es necesario iniciar sesión nuevamente.")
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticación del usuario
        # Si el usuario existe retorna obj usuario, sino, retorna None
        usuarios = authenticate(username=username, password=password)

        if usuarios is not None:
            lgin(request, usuarios)   # inicia sesión
            print(f"ingreso exitoso: {usuarios}")
            msg.success(request, f"Bienvenido {usuarios.username}!")
            # Aquí podrías redirigir a una página de inicio o dashboard
            print(msg.get_messages(request))
            return redirect('index')
        else:
            print("Error de autenticación: usuario o contraseña incorrectos")
            # Aquí podrías redirigir a una página de error o mostrar un mensaje
            msg.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'user/login.html', {})


def logout(request):
    """
    Handle user logout.
    """
    lgout(request)  # Cierra la sesión del usuario
    msg.success(request, "Has cerrado sesión exitosamente.")
    return redirect('index')  # Redirige a la página de bienvenida


def registro(request):
    # verificar request del cliente
    form = Registro(request.POST or None)

    if request.user.is_authenticated:
        msg.info(request, "No es necesario registrarse nuevamente.")
        return redirect('index')

    if request.method == 'POST' and form.is_valid():
        # Procesar el formulario
        user = form.save()
        # si el usuario no retorna None
        if user:
            print(user)
            lgin(request, user)
            msg.success(
                request,
                f"Usuario {user.username} registrado exitosamente!"
                )
            return redirect('index')

    return render(request, 'user/registro.html', {
        'form': form
    })
