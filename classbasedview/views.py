from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Studen

# Create your views here.
# class GreetingView(View):
#     grertingMessage='<b>First CBV From Varible</b>'
#     def get(self,request):
#         return HttpResponse(self.grertingMessage)

class StudentListView(ListView):
    model = Studen
    

