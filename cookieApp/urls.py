from django.urls import path
from cookieApp import views

urlpatterns = [
   
    path('',views.home),
    path('page2/',views.page2),
    path('count/',views.countView),

]
