from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.template import Template

# Create your views here.
def form_css(request):
    return render(request, 'form.css')

def login(request): 
    # add an user verification here
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if the user exists
        user = User.objects.filter(username=username, password=password)
        if user:
            request.session['username'] = username
            return redirect('home/')
        else:
            return HttpResponse('User not found')
    
    context['user_created'] = request.session.get('user_created', False)	
    return render(request, 'login.html', context)

# when the user clicks the login button, the init page is loaded and 
# displays the user's name and password

def init(request):
    name = request.POST.get('username')
    password = request.POST.get('password')
    return render(request, 'text.html', {'name': name, 'password': password})


def register(request):
    
    plantilla = Template('register.html')
    contexto = {'warning': []}


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('mail')
        phone = request.POST.get('celphone')
        is_passenger = request.POST.get('type') == 'Pasajero'
        
        asientos = 0
        if not is_passenger:
            asientos = request.POST.get('n_disponibles')

        user_save = User(username=username,
                        password=password,
                        email=email,
                        phone=phone,
                        is_passenger=is_passenger,
                        asientos_disponibles=asientos)
        # i need verify if the user exists

        user = User.objects.filter(username=username)
        
        if user:
            contexto['warning'].append('Usuario ya existe')
        # create a user object
        if password != password2:
            contexto['warning'].append('Contraseñas no coinciden')

            
        
        if  contexto['warning'] :
            return render(request, 'register.html',contexto)
        
        request.session['user_created'] = True 
        user_save.save()
        return redirect('/',contexto)
    
    return render(request, 'register.html')

def forgot(request):
    contexto = {'warning': []}
    
    # Se recupera la información del formulario
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Se verifica que el usuario exista
        user = User.objects.filter(username=username)
        if not user:
            contexto['warning'].append('Usuario no existe')
        
        # Se verifica que las contraseñas coincidan
        if new_password != confirm_password:
            contexto['warning'].append('Contraseñas no coinciden')
        
        # Si hay errores, se muestran
        if contexto['warning']:
            return render(request, 'forgot.html', contexto)
        
        # Se actualiza la contraseña
        user.update(password=new_password)
        return redirect('login')
    
    return render(request, 'forgot.html')