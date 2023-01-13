from django.shortcuts import render

# Create your views here.


def approveseller(request):
    return render(request,'ecom_admin/approveseller.html')

def home(request):
    return render(request,'ecom_admin/home.html')    

def viewcustomer(request):
    return render(request,'ecom_admin/viewcustomer.html')

def viewseller(request):
    return render(request,'ecom_admin/viewseller.html')      

