from django.shortcuts import render
from django.contrib import messages
from shop.forms import *
from shop.models import Product, Cart
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash



#home page
def homePage(request):
    context = {'products': Product.objects.all() }
    return render(request, 'index.html', context)


#sign up page
def signupPage(request):
    if not request.user.is_authenticated:
        if request.POST:
            frm = MyRegForm(request.POST)
            if frm.is_valid():
                try:
                    frm.save()
                    messages.success(request, 'Your account has been registered')

                except Exception as e:
                    messages.error(request, 'Your account is already registered')

        else:
            frm = MyRegForm()
        return render(request, 'signup.html',{'frm':frm})

    else:
        return HttpResponseRedirect('/')



#login page
def loginPage(request):
    if not request.user.is_authenticated:
        if request.POST:
            frm=MyLoginForm(request=request, data=request.POST)
            if frm.is_valid():
                uname=frm.cleaned_data['username']
                upass=frm.cleaned_data['password']
                user=authenticate(request, username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error_message = 'Invalid username or password.'
                    return render(request, 'login.html',{'error': error_message})
        else:
            frm = MyLoginForm()

        return render(request, 'login.html', {'frm':frm})

    else:
        return HttpResponseRedirect('/')



#logout
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#profile update
def profilePage(request):
    if request.user.is_authenticated:
        if request.POST:
           frm=MyprofileForm(data=request.POST, instance=request.user) 
           if frm.is_valid():
                try:
                    frm.save()
                    messages.success(request, 'Profile update successfully')
                except Exception as e:
                    messages.error(request, 'Profile not update successfully')
        else:
            frm=MyprofileForm(instance=request.user)
        return render(request, 'edit__profile.html', {'frm':frm})
    else:
        return HttpResponseRedirect('/login/') 



#product view page
def productviewPage(request, p_id):
    product = Product.objects.get(p_id= p_id)
    return render(request, 'productview.html', {'product' : product} )


#password change
def changepasswordPage(request):
    if request.user.is_authenticated:
        if request.POST:
            frm=ChangePasswordForm(request.user, request.POST)
            if frm.is_valid():
                try:
                    frm.save()
                    update_session_auth_hash(request, request.user)
                    messages.success(request, 'Password has been changed successfully')
                except Exception as e:
                    messages.error(request, 'Password has not been changed successfully')
        else:
            frm=ChangePasswordForm(request.user)
        return render(request, 'change__password.html',{'frm':frm})
    else:
       return HttpResponseRedirect('/login/') 



#add to cart
def addtocart(request):
    if request.user.is_authenticated:
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        total_price = request.POST.get('total_price')
        customer = request.user.id
        Cart.objects.raw("INSERT INTO shop_cart (product, quantity, total_price, customer) VALUES ({}, '{}', {}, {}, {})".format(product, quantity, total_price, customer))
        
        
        
        return HttpResponseRedirect('/cart-prdt/')
        # return HttpResponse(request.POST)
    else:
        return HttpResponseRedirect('/login/')


def cartview(request):
    if request.user.is_authenticated:
         return render(request, 'cart.html')
    else:
        return HttpResponseRedirect('/login/')

   
