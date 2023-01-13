from django.shortcuts import render
from common.models import Seller
from .models import Product

# Create your views here.


def add_product(request):
    if request.method  == "POST":
        category = request.POST['category']
        product_name = request.POST['product_name']
        product_no = request.POST['product_no']
        product_description = request.POST['product_description']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES['image']
        seller = request.session['seller']
        new_product = Product(category = category,product_name = product_name,product_no = product_no ,

        product_description = product_description, price = price,stock = stock, image = image, seller_id=seller) 
        # seller_id   (when we set a foriegn key it comes with  _id in database)
        new_product.save() 

    return render(request,'seller/add product.html')

def home(request):
    seller_details = Seller.objects.get(id = request.session['seller'])
    products = Product.objects.filter(seller_id = request.session['seller'])
    sname = seller_details.first_name + ' ' + seller_details.last_name
    context = {
        'seller':seller_details,   
        'products' :products,
        'name' : sname 
         }
    
    return render(request,'seller/home.html',context)
     

def product_catalogue(request):
    return render(request,'seller/product catalogue.html') 

def master(request):
    return render(request,'seller/master.html')   

def profile(request):
    return render(request,'seller/profile.html')

def update_stocks(request):
    return render(request,'seller/update stocks.html')  

def view_order(request):
    return render(request,'seller/view order.html')  

def change_password(request):
    error_msg = ''
    success_msg = ''
    if request.method  == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) > 8:
                seller = Seller.objects.get(id = request.session['seller'])
                if old_password == seller.password:
                    seller.password = new_password
                    seller.save()
                    success_msg = 'updated successfully'
                else:
                    error_msg = 'Invalid password'    

            else:
                error_msg = 'Password should be minimum 8 characters'
        
        else :
            error_msg = 'password does\'nt  match'
    

    return render(request,'seller/change password.html',{'error':error_msg,'success':success_msg})

