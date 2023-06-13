"""
URL configuration for clipro project.

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
from django.urls import path, include
from CrudFunc import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #pa#th('/',include('firstapp.urls')),
    # path('quoteapp/',include('quoteapp.urls')),
    path('',include('CrudFunc.urls')),
    # path('classbasedview/',include('classbasedview.urls')),
    # path('cookie/',include('cookieApp.urls')),
    # path('sessionAPI/',include('sessionAPI.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    # path('',views.getStudents,name='getStudents'),
    # path('createStudent/',views.createStudent,name='createStudent'),
    # path('deleteStudent/<int:id>',views.deleteStudent,name='deleteStudent'),
    # path('updateStudent/<int:id>',views.updateStudent,name='updateStudent'),

]
