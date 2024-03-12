from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,cart
from .forms import CreatUserForm,LoginUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def showphone(request):
    template=loader.get_template('showphone.html')
    phone=ItemDetails.objects.select_related('itemsid')
    
    print(phone.query)
    return HttpResponse(template.render({'phone':phone}))

def details(request, id):
    template=loader.get_template('details.html')
    phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'phone':phone,
        'request':request
        }
    return HttpResponse(template.render(context))

def auth_login(request):
    template=loader.get_template('auth_login.html')
    return HttpResponse(template.render())
@csrf_exempt
def auth_register(request):
    template=loader.get_template('auth_register.html')
    form=CreatUserForm()
    if request.method=='POST':
        form=CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform':form,
             'request':request}
    return HttpResponse(template.render(context=context))


@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=='POST':
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,"index.html")
                        
    context={"form":form,
             'request':request}
    return render(request,'auth_login.html',context)

@csrf_exempt
def auth_logout(request):
     if request.method=='POST':
         logout(request)
         return redirect('/')
     
     


def addtocart(requset,id):
     currentuser=requset.user
     discount=6
     state=False
     phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
    
     for item in phone:
           net=item.total-discount
     cartt = cart( #class(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     
     
     currentuser=requset.user.id
     count=cart.objects.filter(Id_user=currentuser).count() #calss Cart
     print(count)
     cartt.save()
     requset.session['countcart']=count
     return redirect("/showphone/")