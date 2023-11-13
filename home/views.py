from django.shortcuts import render
from login.models import User
from home.models import Travels
# Create your views here.
def home(request):
    # get the user object
    user = User.objects.get(username=request.session['username'])
    if request.method == 'POST':
        date = request.POST.get('fecha')
        time = request.POST.get('hora')
        to = request.POST.get('destino')
        person = User.objects.get(username=request.session['username'])

        # create a travel object
        new_travel = Travels(date=date, time=time, to=to, driver=person)
        new_travel.save()

    context = {'name': request.session['username']}
    context['user'] = user
    return render(request, 'welcome.html',context)

def logout(request):
    del request.session
    return render(request, 'login.html')

def history_travel(request):
    user = User.objects.get(username=request.session['username'])
    # Obtain the informa
    travels = Travels.objects.all()
    context = {'travels': travels}
    context['user'] = user
    return render(request, 'history_travel.html', context)   


def new_travel(request):
    context = {'name': request.session['username']}
    user = User.objects.get(username=request.session['username'])
    context['user'] = user
    return render(request, 'new_travel.html',context)

def contact(request):
    context = {'name': request.session['username']}
    
    user = User.objects.get(username=request.session['username'])
    context['user'] = user
    # Obtain the informa
    # user = User.objects.filter  , , {'users': user}
    return render(request, 'contact.html',context)