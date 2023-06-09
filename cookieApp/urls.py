from django.urls import path
from cookieApp import views

urlpatterns = [
   
    path('',views.home),
    path('page2/',views.page2),
    path('count/',views.countView),
    path('index/',views.index),
    path('addItem/',views.addItem),
    path('displayItems/',views.displayCart),

]
