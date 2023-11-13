from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.template import Template

# Create your views here.
def form_css(request):
    return render(request, 'form.css')

def login(request): 
    # add an user verification here

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

    return render(request, 'login.html')

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

        user_save = User(username=username, password=password, email=email, phone=phone)
        # i need verify if the user exists

        user = User.objects.filter(username=username)
        
        if user:
            contexto['warning'].append('Usuario ya existe')
        # create a user object
        if password != password2:
            contexto['warning'].append('Contraseñas no coinciden')

            
        
        if  contexto['warning'] :
            return render(request, 'register.html',contexto)
        
        contexto['user_created'] = True 
        user_save.save()
        return redirect('',contexto)
    
    return render(request, 'register.html')



    