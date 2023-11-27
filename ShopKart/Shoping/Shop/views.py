from django.shortcuts import render, redirect
from Shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'Shop/index.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out Successfully')
        return redirect('/')

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("/")
            else:
                messages.error(request, 'Invalid User Name or Password')
                return redirect("/login")
        return render(request, 'shop/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        forms=CustomUserForm()
        if request.method=='POST':
            forms=CustomUserForm(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Registration successful you can Login now')
                return redirect('/login')
        return render(request, 'shop/register.html', {'forms':forms})

def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request, 'shop/collections.html', {'catagory':catagory})

def collectionsview(request, name):
    if(Catagory.objects.filter(name=name, status=0)):
        products=Product.objects.filter(catagory__name=name)
        return render(request, "Shop/products/index.html", {'products':products, 'catagory_name':name})
    else:
        messages.warning(request, "No Such Catagory Found")
        return redirect('collections')
    
def product_details(request, catagoryname, productname):
    if(Catagory.objects.filter(name=catagoryname, status=0)):
        if(Product.objects.filter(name=productname, status=0)):
            products=Product.objects.filter(name=productname, status=0).first()
            return render(request,"Shop/products/product_details.html", {'products':products})
        else:
            messages.error(request, "No Such Product Found")
            return redirect('collections')
    else:
            messages.error(request, "No Such Product Found")
            return redirect('collections')