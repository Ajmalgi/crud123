from django.shortcuts import render,redirect
from common.models import Customer
from seller.models import Product
from .models import Cart
from django.http import JsonResponse
from. decorater  import auth_customer



# Create your views here.
@auth_customer
def change_password(request):
    error_msg = ''
    success_msg = ''
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) > 8:
                customer = Customer.objects.get(id = request.session['customer'])
                if old_password == customer.password:
                    Customer.objects.filter(id = request.session['customer']).update(password = new_password)
                   
                    success_msg = 'updated successfully'
                else:
                    error_msg = 'Invalid password'    

            else:
                error_msg = 'Password should be minimum 8 characters'
        
        else :
            error_msg = 'password does\'nt  match'
    



    return render(request,'customer/change password.html',{'success':success_msg,'error':error_msg})


def checkout(request):
    return render(request,'customer/checkout.html')

@auth_customer
def home(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    products = Product.objects.all()
    cname = customer_details.first_name + ' ' + customer_details.last_name
    context = {
        'name':cname,
        'products':products

    }
    return render(request,'customer/home.html',context)    

def myorders(request):
    return render(request,'customer/myorders.html')  

@auth_customer
def productdetails(request,pid):
    product_details = Product.objects.get(id = pid)
    msg = ''
    if request.method == 'POST':
        item = Cart.objects.filter(customer = request.session['customer'],product = pid).exists()
        if not item:           #same as if item == false:

            cart_item = Cart(customer_id = request.session['customer'],product_id = pid)
            cart_item.save()
            return redirect('customer:cart')
        else:
            msg = 'Item already in cart'


    return render(request,'customer/productdetails.html',{'details':product_details,'message':msg})
    

def profile(request):
    return render(request,'customer/profile.html')  

@auth_customer
def mycart(request): 
    items = Cart.objects.filter(customer_id = request.session['customer'])
    return render(request,'customer/mycart.html',{'items':items})

    
  
def get_total_price(request):
    pid = request.POST['pid']    #pid is the key passed from ajax request
    qty = request.POST['qty']
    product = Product.objects.filter(id = pid).values('price')
    total_amount = int(qty) * product[0]['price']
    print(total_amount)
    return JsonResponse({'amount': total_amount})

def remove_cart_item(request,cid):
    item = Cart.objects.get(id = cid)
    item.delete()
    return redirect('customer:cart')


def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:home')