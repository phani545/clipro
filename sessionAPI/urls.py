from django.urls import path
from sessionAPI import views 


urlpatterns = [
    # path('hello/',v.display,name='display'),
    # path('time/',v.displayDateTime,name='displayDateTime'),

   
    path('',views.pageCount),
    path('index/',views.index),
    path('addItem/',views.addItem),
    path('displayItems/',views.displayCart),   
    
    

]
