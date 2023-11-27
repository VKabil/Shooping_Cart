from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logout', views.logout_page, name='logout'),
    path('login', views.login_page, name='login'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:name>', views.collectionsview, name='collections'),
    path('collections/<str:catagoryname>/<str:productname>', views.product_details, name='product_details'),
]