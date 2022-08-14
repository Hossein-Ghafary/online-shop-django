from django.shortcuts import render
from . models import Shop
# Create your views here.


def shop(request):
    product_list = Shop.objects.all()
    context = {
        'shop' : product_list
    }
    return render(request,"shop/shop.html",context)


def shop_detail(request,id):
    product_list = Shop.objects.get(id=id)
    context = {
            'shop' : product_list
    }
    return render(request,"shop/detail.html",context)