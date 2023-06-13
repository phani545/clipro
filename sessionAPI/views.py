from django.shortcuts import render
from .forms import ItemForm

# Create your views here.
def pageCount(request):
    count = request.session.get('count',0)
    count = count + 1
    raise Exception("Something happens in the system")
    request.session['count']=count
    return render(request,'sessionApp/count.html',{'count':count})


def index(request):
    request.session.set_expiry(180)
    #del request.session['count']
    
    return render(request,'sessionApp/index.html')

def addItem(request):
    form=ItemForm()
    #response = render(request, 'sessionApp/addItem.html',{'form':form})
    if request.method=='POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quantity=form.cleaned_data['quantity']
            request.session[name]=quantity
            #response.set_cookie(name,quantity,120)
    return render(request, 'sessionApp/addItem.html',{'form':form})


def displayCart(request):
    return render(request,'sessionApp/displayItems.html')
