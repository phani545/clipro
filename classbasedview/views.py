from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import Studen
from django.urls import reverse_lazy


# Create your views here.
# class GreetingView(View):
#     grertingMessage='<b>First CBV From Varible</b>'
#     def get(self,request):
#         return HttpResponse(self.grertingMessage)

class StudentListView(ListView):
    model = Studen
#default template_name is studen_list.html
# default context_object_name is studen_list

class StudentDetailView(DetailView):
    model = Studen
#default template_name is studen_detail.html
# default context_object_name is studen_list

class StudentCreateView(CreateView):
    model = Studen
    fields = {'firstName','lastName','testscore'}
#default template_name is studen_form.html
# default context_object_name is studen_list

class StudentUpdateView(UpdateView):
    model = Studen
    fields = {'testscore'}

class StudentDeleteView(DeleteView):
    model = Studen
    success_url=reverse_lazy('students')

#default template_name is studen_form.html
# default context_object_name is studen_list






