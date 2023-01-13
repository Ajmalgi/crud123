from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('change_password',views.change_password,name='password'),
    path('checkout',views.checkout,name='check'),
    path('home',views.home,name='home'),
    path('myorders',views.myorders,name='orders'), 
    path('productdetails/<int:pid>',views.productdetails,name='details'), 
    path('profile',views.profile,name='profile'),
    path('mycart',views.mycart,name='cart'),
    path('get_total_amount',views.get_total_price,name='total_price'),
    path('remove_cart/<int:cid>',views.remove_cart_item,name='remove_cart'),
    path('logout',views.logout,name='logout'),
]