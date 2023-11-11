from django.shortcuts import render
from login.models import User
# Create your views here.
def home(request):

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