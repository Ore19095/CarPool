from django.shortcuts import render
from login.models import User
from home.models import Travels

from datetime import datetime
# Create your views here.
def home(request):
    # get the user object
    user = User.objects.get(username=request.session['username'])
    if request.method == 'POST':
        date = request.POST.get('fecha')
        time = request.POST.get('hora')
        to = request.POST.get('destino')
        free = user.asientos_disponibles
        person = User.objects.get(username=request.session['username'])

        # create a travel object
        new_travel = Travels(date=date, time=time, to=to, driver=person,
                                free_seats=free)
        new_travel.save()

    context = {'name': request.session['username']}
    context['user'] = user
    return render(request, 'welcome.html',context)

def logout(request):
    del request.session
    return render(request, 'login.html')

def history_travel(request):
    user = User.objects.get(username=request.session['username'])
    # se hizo una peticion de tipo POST
    if request.method == 'POST':
        travel_id = request.POST.get('travel_id')
        add = request.POST.get('add')
        print(travel_id)
        # objeter el viaje segun el id
        travel = Travels.objects.get(id=travel_id)
        if add == '2': # elimina el viaje
            travel.delete()
        if add == '1':
            travel.passengers.add(user)
            travel.free_seats -= 1
        if add == '0':
            travel.passengers.remove(user)
            travel.free_seats += 1
        
        if travel.free_seats >= 0 and user.is_passenger:
            travel.save()
        # a

    # Obtain the informa
    travels = Travels.objects.all()

    valid_travels = []
    my_travels = []
    context ={}
    now = datetime.now()
    # si el usuario es pasajero
    if user.is_passenger:
        for travel in travels:
            if travel.date > now.date() and travel.time > now.time() \
                and user not in travel.passengers.all() and travel.free_seats > 0:
                valid_travels.append(travel)

        for travel in travels:
            if travel.date > now.date() and travel.time > now.time() \
                and user  in travel.passengers.all():
                my_travels.append(travel)
        context['my_travels'] = my_travels
    else:
        # muestra mis viajes activos
        all = []
        for travel in travels:
            if travel.date > now.date() and travel.time > now.time() \
                and travel.driver == user:
                data = [travel, [a for a in travel.passengers.all()]]
                print(data[1])
                all.append(data)
        context['my_travels'] = all




    context['travels']= valid_travels
    
    context['user'] = user
    return render(request, 'history_travel.html', context)   


def new_travel(request):
    context = {'name': request.session['username']}
    user = User.objects.get(username=request.session['username'])
    context['user'] = user
    return render(request, 'new_travel.html',context)

def about_us(request):
    context = {'name': request.session['username']}
    
    user = User.objects.get(username=request.session['username'])
    context['user'] = user
    # Obtain the informa
    # user = User.objects.filter  , , {'users': user}
    return render(request, 'about_us.html',context)