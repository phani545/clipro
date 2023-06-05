from django.urls import path
from CrudFunc import views 


urlpatterns = [
    # path('hello/',v.display,name='display'),
    # path('time/',v.displayDateTime,name='displayDateTime'),

   
    path('',views.getStudents,name='getStudents'),
    path('createStudent/',views.createStudent,name='createStudent'),
    
    
    

]
