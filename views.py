from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,cart
from django.contrib.auth.decorators import login_required
#from rest_framework.decorators import api_viewrt 
# Create your views here.

def showplants(request):
    template=loader.get_template('showplants.html')
    plant=ItemDetails.objects.select_related('itemsid')
    
    print(plant.query)
    return HttpResponse(template.render({'plant':plant, 'request':request}))
    


def P_details(request, id):
    template=loader.get_template('P_details.html')
    plant=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'plant':plant,
        'request':request
        }
    return HttpResponse(template.render(context))


@login_required(login_url='/auth_login/')
def checkout(request):
       template=loader.get_template('checkout.html')
       current_user = request.user.id
       cartt=cart.objects.all().filter(Id_user=current_user).first()
       product=Items.objects.get(id=cartt.Id_product)
       context={
            'cartt':cartt,
            'productname':product,
            'request':request
            
       }
       return HttpResponse(template.render(context=context)) 
    

def add_to_cart(requset,id):
     currentuser=requset.user
     discount=6
     state=False
     plant=ItemDetails.objects.select_related('itemsid').filter(id=id)
     count=0
     for item in plant:
        net=item.total-discount
        count=count+1
     cartt = cart( #class(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      length=item.length,
      image=item.image,
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
     requset.session['countcartt']=count
     return redirect('/showplants/')

 