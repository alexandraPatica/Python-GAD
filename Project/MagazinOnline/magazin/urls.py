from django.urls import path
from magazin.views import products, add_product, add_product_to_cart, view_cart

app_name = 'products'

# this is in `/products/`
urlpatterns = [
    path('', products, name='view_all'),
    path('add/', add_product, name='add'),
    path('<int:product_id>/add_to_cart/', add_product_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart')
]