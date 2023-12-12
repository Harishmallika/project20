"""
URL configuration for project20 project.

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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootstrap1/',bootstrap1,name='bootstrap1'),
    path('bootstrap2/',bootstrap2,name='bootstrap2'),
    path('buttons/',buttons,name='buttons'),
    path('buttons1/',buttons1,name='buttons1'),
    path('buttons2/',buttons2,name='buttons2'),
    path('buttons3/',buttons3,name='buttons3'),
    path('buttons4/',buttons4,name='buttons4'),
    path('buttons5/',buttons5,name='buttons5'),
    path('buttons6/',buttons6,name='buttons6'),
    path('buttons7/',buttons7,name='buttons7'),
    path('buttons8/',buttons8,name='buttons8'),
    path('buttons9/',buttons9,name='buttons9'),
    path('buttons10/',buttons10,name='buttons10'),
    path('buttons11/',buttons11,name='buttons11'),
    path('button_group/',button_group,name='button_group'),
    path('button_group1/',button_group1,name='button_group1'),
    path('button_group2/',button_group2,name='button_group2'),
    path('button_group3/',button_group3,name='button_group3'),
    path('button_group4/',button_group4,name='button_group4'),
    path('card/',card,name='card'),
    path('card1/',card1,name='card1'),
    path('card2/',card2,name='card2'),
    path('card3/',card3,name='card3'),
    path('card4/',card4,name='card4'),
    path('card5/',card5,name='card5'),
    path('card6/',card6,name='card6'),
    path('card7/',card7,name='card7'),
    path('card8/',card8,name='card8'),
    path('card9/',card9,name='card9'),
    path('card10/',card10,name='card10'), 
    path('card11/',card11,name='card11'), 
    path('card12/',card12,name='card12'), 
    path('card13/',card13,name='card13'), 
    path('card14/',card14,name='card14'),
    path('card15/',card15,name='card15'),
    path('card16/',card16,name='card16'),
    path('card17/',card17,name='card17'),
    path('card18/',card18,name='card18'),
    path('card19/',card19,name='card19'),
    path('card20/',card20,name='card20'),
    path('card21/',card21,name='card21'),
    path('card22/',card22,name='card22'),
    path('card23/',card23,name='card23'),
    path('card24/',card24,name='card24'),
    path('card25/',card25,name='card25'),
    path('card26/',card26,name='card26'),
    path('card27/',card27,name='card27'),
    path('card28/',card28,name='card28'),
    path('card29/',card29,name='card29'),
    path('card30/',card30,name='card30'),
    path('card31/',card31,name='card31'),
    path('carousel/',carousel,name='carousel'),
    path('carousel1/',carousel1,name='carousel1'),
    path('harish90/',harish90,name='harish90'),
    path('index/',index,name='index'),









]
