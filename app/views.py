from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Cart

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html",locals())
    
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    return render(request, 'app/addtocart.html', locals())