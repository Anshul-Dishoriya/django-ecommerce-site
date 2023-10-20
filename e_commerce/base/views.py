from django.shortcuts import render, redirect
from .models import Product, Cart, Order
from .custom_ml_algo import K_Nearest_Neighbor
from .utils import create_model_predict_products , get_products


# View to display a list of products
def product_list(request):
    products = Product.objects.all()
    return render(request, "base/all_products.html", {"products": products})


# View to Add the product
def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        description = request.POST.get("description")
        prod = Product(
            name=name, description=description, category=category, price=price
        )
        prod.save()
        return redirect("all-products")
    return render(request, "base/add_product.html")


# View to display a user's cart
def view_cart(request):
    products = Cart.objects.all()
    return render(request, "base/cart.html", {"products": products})


def view_product_recomendation(request):
    data = create_model_predict_products()
    products = get_products(data)
    return render(request, "base/recom_product.html" ,{'products':products})


# View to add a product to the user's cart
def add_to_cart(request, product_id):
    prod = Product.objects.get(id=product_id)
    cart, flag = Cart.objects.get_or_create(products=prod)
    if not cart:
        cart.add(prod)
    return redirect("view-cart")


# View to remove a product from the user's cart
def remove_from_cart(request, product_id):
    prod = Product.objects.get(id=product_id)
    cart_item = Cart.objects.filter(products=prod)
    cart_item.delete()
    return redirect("view-cart")


# View for the checkout process
def checkout(request, product_id):
    prod = Product.objects.get(id=product_id)
    order, flag = Order.objects.get_or_create(products=prod)
    if not flag:
        order.add(prod)
    return redirect("view-orders")


# View to get all the orders
def view_orders(request):
    orders = Order.objects.all()
    return render(request, "base/orders.html", {"orders": orders})


# View to place order for a product
def add_to_orders(request, product_id):
    print("asdasdasd")
    prod = Product.objects.get(id=product_id)
    order, flag = Order.objects.get_or_create(products=prod)
    if not order:
        order.add(prod)
    return redirect("view-orders")


def remove_from_orders(request, product_id):
    prod = Product.objects.get(id=product_id)
    order_item = Order.objects.filter(products=prod)
    order_item.delete()
    return redirect("view-orders")
