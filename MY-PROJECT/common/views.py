from django.shortcuts import render , redirect
from .models import Customer
from .models import Seller
from random import randint
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def admin_logo(request):
     return render(request,'common/admin logo.html')

def customer_login(request):
    msg = ''
    if request.method  == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try: 
            customer = Customer.objects.get(email = email, password = password)   #model_name= post_name
            request.session['customer'] = customer.id     # to add session
            return redirect('customer:home') #redirect(app_name:url_name)
        except Exception as e:
            print (e)   #to check error
            msg = 'Invalid credentials'

    return render(request,'common/customer login.html',{'message':msg})
    

def customer_signup(request):
    if request.method  == "POST":
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        new_customer = Customer(first_name = fname,last_name = lname , 
        email = email,password = password, address = address, phone = phone)
        new_customer.save()  #corresponding query of insert
    return render(request,'common/customer signup.html')

def home(request):
    return render(request,'common/home.html') 

def seller_login(request):
    msg = ''
    if request.method  == "POST":
        seller_id = request.POST['seller_id']
        password = request.POST['password']
        try: 
            seller = Seller.objects.get(user_name = seller_id, password = password)
            request.session['seller'] = seller.id  
            return redirect('seller:home') #redirect(app_name:url_name)
        except:
            msg = 'Invalid credentials'

    return render(request,'common/seller login.html',{'message':msg})


def seller_signup(request):
    msg = ''
    if request.method  == "POST":
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        bank_name = request.POST['bank']
        branch = request.POST['branch']
        ifsc = request.POST['ifsc']
        account = request.POST['account']
        seller_pic = request.FILES['seller_pic']
        user_name = randint(1111,9999)
        password = 'sell-' + str(user_name) + '-' + phone[6:10]
    
        new_seller = Seller(first_name = fname,last_name = lname , 
        email = email,password = password, address = address, phone = phone,user_name = user_name,
        bank_name = bank_name, branch = branch,ifsc = ifsc,account_no = account,seller_pic =seller_pic)
        new_seller.save()
        msg = 'Account created successfully'
        email_subject = 'Account username and password'
        email_content = 'Hai your username will be  ' + str(user_name) + 'and password will be' + password

        send_mail(
            email_subject,
            email_content,
            settings.EMAIL_HOST_USER,
            [email,]
        )
    return render(request,'common/seller signup.html',{'message': msg})                 