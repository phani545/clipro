from django.shortcuts import render,redirect
from .models import Studen
from CrudFunc.forms import StudentForm
# Create your views here.

def getStudents(request):
    students=Studen.objects.all() 
    return render(request,'crudApp/index.html',{'students':students})

def createStudent(request):
    form=StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('CrudFunc/')
        return getStudents(request)
    return render(request,'crudApp/createform.html',{'form':form})

def deleteStudent(request,id):
    stud = Studen.objects.get(id=id) 
    stud.delete()
    return getStudents(request)


def updateStudent(request,id):    
    stud = Studen.objects.get(id=id) 
    form=StudentForm(instance=stud)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return getStudents(request)
    return render(request,'crudApp/updateform.html',{'form':form})





