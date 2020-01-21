"""db_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('clients/', include('clients.urls')),
    path('animals/', include('animals.urls')),
    path('species/', include('species.urls')),
    path('vets/', include('vets.urls')),
    path('diagnoses/', include('diagnoses.urls')),
    path('appointments/', include('appointments.urls')),
    path('medicalprocedures/', include('medicalprocedures.urls')),
    path('medications/', include('medications.urls')),
    path('notes/', include('notes.urls')),
    path('diagnosesmedications/', include('diagnosesmedications.urls')),
    path('dignosesprocedures/', include('diagnosesprocedures.urls')),
    
    
]

urlpatterns += staticfiles_urlpatterns() 
