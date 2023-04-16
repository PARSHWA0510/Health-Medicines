from urllib import request
from django.http import JsonResponse
from django.shortcuts import render,redirect
from store.models import Auth_User as au,Product as p,Cart_generator as cg,Cart_Item as ci
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
global userID
userID = -1
def login(request):
    return render(request, 'login.html')

def auth(request):
    global userID
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = au.objects.filter(email=email, password=password).first()
        if user:
            products = p.get_all_products()
            userID = user.id
            return render(request, 'home.html',{"products":products})
        else:
            return render(request, 'login.html',{"msg":"user not found!!"})
    else:
        products = p.get_all_products()
        if userID != -1:return render(request, 'home.html',{"products":products})
        return render(request, 'login.html',{"msg":"Sme error occured!!"})

def register(request):
    return render(request, 'register.html')

def register_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        user = au.objects.filter(email=email).first()
        if user:
            return render(request, 'register.html',{"msg":"Email already registered!!"})
        else:
            user = au(email=email,password=password,name=name,phone=phone,address=address)
            user.save()
            return render(request, 'login.html',{"msg":"Registration successful!"})
       
def open_cart(request):
    cartObj = cg.get_cart(userID)
    if cartObj is None:
        return render(request, 'cart.html',{"msg":"Nothing in cart right now"})
    else:
        grand_total(request)
        cartObj = cg.get_cart(userID)
        cartItems = cg.get_cart_items(cartObj.cart_id)
        if len(cartItems) == 0:
            cartObj.delete()
            cartItems.delete()
            return render(request, 'cart.html',{"msg":"Nothing in cart right now"})
        return render(request, 'cart.html',{"cart_items":cartItems,"cart_gen":cartObj})

def shop_single(request,id):
    context={}
    context["product"]=p.objects.get(id=id)
    return render(request,'shop-single.html',context)


   

    


