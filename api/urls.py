from django.urls import path

from api.views import ProductdetailApiview, UserListApiview, UserdetailApiview, productListApiview 

urlpatterns=[
    path('users/',UserListApiview.as_view()),
    path('users/<int:pk>/',UserdetailApiview.as_view()),
    path('products/',productListApiview.as_view()) ,
    path('products/<int:pk>/',ProductdetailApiview.as_view())

]