"""
URL configuration for shopping project.

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
from django.urls import path#,include
from phone import views
from Plants import views as v2



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name='index'),
    path("showphone/",views.showphone,name='showphone'),
    path('details/<int:id>/',views.details,name='details'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_logout/',views.auth_logout,name='auth_logout'),
    #path('checkout/',views.checkout,name='checkout'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    
    
    #paths of Plants App
    #path('Plants/',include('Plants.urls'))
    
    path('showplants/',v2.showplants,name="showplants"),
    path('checkout/',v2.checkout,name="checkout"),
    path('P_details/<int:id>/',v2.P_details,name="P_details"),
    path('add_to_cart/<int:id>/',v2.add_to_cart,name="add_to_cart")
    
]
