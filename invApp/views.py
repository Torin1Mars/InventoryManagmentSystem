from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product


# Create your views here.
#Home
def home_view(request):
    return render(request, "invApp/home.html" )

#Create view
def product_create_view(request):
    form = ProductForm()

    if request.method =="post":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    return redirect(request, 'invApp/product_form.html', {"form":form})

#Read view
def product_list_view(request):
    products = Product.objects.all()
    return render(request, "invApp/product_list.html", {"products":products})

#Update
def product_update_view(request, productId):
    product = Product.objects.get(product_id = productId)
    form = ProductForm()

    if request.method == "post":
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    return redirect(request, 'invApp/product_form.html', {"form":form})

def product_delete_view(request, productId):
    product = Product.objects.get(productId= productId)
    if request.method == "post":
        product.delete()
        return redirect("product_list")

    return render(request, "invApp/product_confirm_delete.html", {"product":product})

