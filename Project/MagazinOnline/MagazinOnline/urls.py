"""MagazinOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from magazin.views import homepage, products, add_product, add_product_to_cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('shop/products/', include('magazin.urls'))
    # path('magazin/', products),
    # path('magazin/add/', add_product),
    # path('magazin/<int:product_id>/add_to_cart/', add_product_to_cart),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
