from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product-detail', productdetail, name='product-detail'),
    path('my-account', myaccount, name='my-account'),
    path('cart', cart, name='cart'),
    path('login', login, name='login'),
    path('contact', contact, name='contact'),
    path('product-list', productlist, name='product-list'),
    path('wishlist', wishlist, name='wishlist'),
    path('checkout', checkout, name='checkout')
]