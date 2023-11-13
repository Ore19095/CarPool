from django.shortcuts import render
from login.models import User
from home.models import Travels
# Create your views here.
def home(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        to = request.POST.get('destino')
        person = User.objects.get(username=request.session['username'])

        # create a travel object
        new_travel = Travels(date=date, time=time, to=to, person=person)
        new_travel.save()

    context = {'name': request.session['username']}

    return render(request, 'welcome.html',context)

def logout(request):
    del request.session['username']
    return render(request, 'login.html')

def history_travel(request):
    
    return render(request, 'history_travel.html')

def new_travel(request):
    return render(request, 'new_travel.html')

def contact(request):
    # Obtain the informa
    # user = User.objects.filter  , , {'users': user}
    return render(request, 'contact.html')