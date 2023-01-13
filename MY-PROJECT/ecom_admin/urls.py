from django.urls import path
from.import views

urlpatterns=[
    path('approveseller',views.approveseller),
    path('home',views.home),
    path('viewcustomer',views.viewcustomer),
    path('viewseller',views.viewseller),
]
    