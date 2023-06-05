from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee,Project
import datetime
from firstapp.forms import ProjectForm,UserRegistrationForm

# Create your views here.
# def display(request):
#     return HttpResponse('<h1>myfirst view</h1>')


# def displayDateTime(request):
#     dt=datetime.datetime.now()
#     s="<b>Current Date and Time:</b>" + str(dt)
#     return HttpResponse(s)

# def renderTemplate(request):
#     myDict = {"id":123,"name":"Phani","salary":25000}
#     return render(request, 'templatesApp/firsttemplate.html',context=myDict)

def electronics(request):
    product_dic = {
        "product1":'Mac',
        "product2":'IPhone',   
        "product3":'OnePlus',     
    }

    return render(request, 'templatesApp/product.html',product_dic)

def toys(request):
    product_dic = {
        "product1":'Mac',
        "product2":'bus',  
        "product3":'Doll',       
    }

    return render(request, 'templatesApp/product.html',product_dic)

def shoes(request):
    product_dic = {
        "product1":'rebook',
        "product2":'nike',    
        "product3":'Spark',          
    }

    return render(request, 'templatesApp/product.html',product_dic)

def index(request):
    return render(request,'modelApp/index.html')
    #return render(request, 'templatesApp/index.html')

def listProjects(request):
    projectList = Project.objects.all()
    return render(request,'modelApp/listProjects.html',{'projects':projectList})

def addProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'modelApp/addProjects.html',{'form':form})




def employeedata(request):
    employees=Employee.objects.all()
    empDict = {'employees':employees}
    return render(request,'/employees.html',empDict)

def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("FirstName",form.cleaned_data['firstName'])
            print("lastName",form.cleaned_data['lastName'])
            print("email",form.cleaned_data['email'])
    return render(request,'formsApp/userregistration.html',{'form':form})




