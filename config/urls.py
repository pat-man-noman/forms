"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
import app.views
urlpatterns = [
    path("",app.views.hey, name="hey"),
    path("age-in/",app.views.age, name="age"),
    path("order-total/",app.views.order,name="order"),
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    path("font-times",app.views.font, name="font"),
    path("no-teen-sum",app.views.teen, name="teen"),
    path("xyz-there",app.views.xyz, name="xyz"),
    path("centered-average",app.views.centered,name="centered"),
    path('admin/', admin.site.urls),
]
