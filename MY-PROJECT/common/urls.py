from django.urls import path
from.import views
app_name = 'common'

urlpatterns=[
    path('admin_logo',views.admin_logo),
    path('customer_login',views.customer_login,name='clogin'),
    path('customer_signup',views.customer_signup,name='csign'),
    path('home',views.home,name='home'),
    path('seller_login',views.seller_login,name='slogin'),
    path('seller_signup',views.seller_signup,name='ssign'),
]