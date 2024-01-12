
from django.urls import path,include
from ContactBookApp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addcontact/',views.createct,name='createct'),
    path('dispall/',views.contactlist, name='contactlist'),
    path('dispall/details/<int:id>/',views.contactdetails,name='contactdetails'),
    path('dispall/updatect/<int:id>/',views.updatect,name='updatect'),
    path('dispall/deletect/<int:id>/',views.deletect,name='deletect'),
    path('findcontact/',views.search,name='search'),
]
