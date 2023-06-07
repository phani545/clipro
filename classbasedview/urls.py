from django.urls import path
from classbasedview import views 

urlpatterns = [
    # path('hello/',v.display,name='display'),
    # path('time/',v.displayDateTime,name='displayDateTime'),

    #path('',views.GreetingView.as_view(grertingMessage='<b>First CBV from Attribute</b>')),

    path('',views.StudentListView.as_view(),name='students'),
    path('<int:pk>/',views.StudentDetailView.as_view(),name='detail'),
    path('create/',views.StudentCreateView.as_view()),
    path('update/<int:pk>/',views.StudentUpdateView.as_view()),
    path('delete/<int:pk>/',views.StudentDeleteView.as_view()),

]
