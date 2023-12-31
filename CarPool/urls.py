"""
URL configuration for CarPool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import login.views
import home.views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.views.login, name='login'),
    path('init/', login.views.init, name='init'),
    path('registry/', login.views.register, name='register'),
    path('forgot/', login.views.forgot, name='forgot'),
    path('home/', home.views.home, name='home'),
    path('logout/', home.views.logout, name='logout'),
    path('home/about_us/', home.views.about_us, name='About us'),
    path('home/new_travel/', home.views.new_travel, name='new_travel'),
    path('home/history_travel/', home.views.history_travel, name='history_travel'),
]
