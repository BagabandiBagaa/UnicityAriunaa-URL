from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.shortcuts import render, redirect
from .forms import OrderForm

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'products/success.html')
    else:
        form = OrderForm()
    return render(request, 'products/order.html', {'form': form})
def index(request):
    item_list = Item.objects.all()
    context ={
        'item_list':item_list
    }
    return render(request,'products/main.html',context)
def sortt(request,item_type):
    item_list = Item.objects.all()
    item_sortt = item_list.filter(item_type=item_type)
    context ={
        'item_sortt':item_sortt
    }
    return render(request,'products/sortt.html',context)
def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    return render(request,'products/details.html',context)
def about(request):
    return render(request,'products/about.html')
def success(request):
    return render(request,'products/success.html')
def contact(request):
    return render(request,'products/contact.html')

