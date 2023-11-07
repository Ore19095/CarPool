from django.shortcuts import render

# Create your views here.
def home(request):

    context = {'name': request.session['username']}

    return render(request, 'welcome.html',context)

def logout(request):
    del request.session['username']
    return render(request, 'login.html')

def new_travel(request):
    return render(request, 'travel.html')