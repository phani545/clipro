from django.urls import path
from classbasedview import views 

urlpatterns = [
    # path('hello/',v.display,name='display'),
    # path('time/',v.displayDateTime,name='displayDateTime'),

    #path('',views.GreetingView.as_view(grertingMessage='<b>First CBV from Attribute</b>')),

    path('',views.StudentListView.as_view()),
]
