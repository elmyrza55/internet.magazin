from marketplace.models import Category,Product
from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'index.html',
    {'categories':categories})

def suit(request):
    products = products.all()
    categories = Category.objects.all()
    title = 'Костюм'
    return render(request,'suit.html',{'title':title,
    'products':products, 'categories':categories})
    
def cart(request):
    return render(request, 'cart.html', {'title':'Корзина'} )