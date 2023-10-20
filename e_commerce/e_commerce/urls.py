from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.product_list, name="all-products"),
    path("product/<int:product_id>", views.product_list, name="view-product"),
    path("add-product/", views.add_product, name="add-product"),
    
    path("cart/", views.view_cart, name="view-cart"),
    path("cart/<int:product_id>", views.add_to_cart, name="add-cart"),
    path("remove-cart/<int:product_id>", views.remove_from_cart, name="remove-cart"),

    path("orders", views.view_orders, name="view-orders"),
    path("orders/<int:product_id>", views.add_to_orders, name="add-order"),
    path("cancel-order/<int:product_id>", views.remove_from_orders, name="cancel-order"),
 
    path("prod-recomendation", views.view_product_recomendation, name="rec-products"),
]
