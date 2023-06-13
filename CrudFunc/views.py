from django.shortcuts import render,redirect
from .models import Studen
from CrudFunc.forms import StudentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def getStudents(request):
    students=Studen.objects.all() 
    return render(request,'crudApp/index.html',{'students':students})

@login_required
def createStudent(request):
    form=StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('CrudFunc/')
        return getStudents(request)
    return render(request,'crudApp/createform.html',{'form':form})

@login_required
def deleteStudent(request,id):
    stud = Studen.objects.get(id=id) 
    stud.delete()
    return getStudents(request)

@login_required
def updateStudent(request,id):    
    stud = Studen.objects.get(id=id) 
    form=StudentForm(instance=stud)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return getStudents(request)
    return render(request,'crudApp/updateform.html',{'form':form})


def logout(request):
    return render(request,'registration/logout.html')





