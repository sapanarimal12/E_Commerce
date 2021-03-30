from django.shortcuts import render
from django.views.generic.base import View
from .models import *

# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.filter(status='active')
        self.views['sliders'] = Slider.objects.filter(status='active')
        self.views['brands'] = Brand.objects.filter(status='active')
        self.views['ads'] = Ad.objects.all
        self.views['hot items'] = Item.objects.filter(label='hot')
        self.views['new items'] = Item.objects.filter(label='new')
        self.views['sale items'] = Item.objects.filter(label='sale')
        self.views['default items'] = Item.objects.filter(label='')

        return render(request, 'index.html', self.views)


def myaccount(request):
    return render(request, 'my-account.html')
def productdetail(request):
    return render(request, 'product-detail.html')
def cart(request):
    return render(request, 'cart.html')
def login(request):
    return render(request, 'login.html')
def contact(request):
    return  render(request,'contact.html')
def productlist(request):
    return render(request, 'product-list.html')
def wishlist(request):
    return render(request, 'wishlist.html')
def checkout(request):
    return render(request, 'checkout.html')







