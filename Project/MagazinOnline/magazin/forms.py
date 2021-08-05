from django import forms
from magazin.models import Products, Order, OrderProduct


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = []


class FilterProducts(forms.Form):
    has_image = forms.BooleanField(label='Filter only products with image')
    min_price = forms.FloatField(label='Min Price', required=False)
    max_price = forms.FloatField(label='Max Price', required=False)

    def get_products(self):
        products = Products.objects.all()
        filter_products_with_image = self.cleaned_data.get('has_image', False)
        min_price = self.cleaned_data.get('min_price')
        max_price = self.cleaned_data.get('max_price')

        if filter_products_with_image:
            products = products.exclude(img=None)

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        return products


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'shipping_address', 'email']

    def __init__(self, products, cart_data, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.products = products
        self.cart_data = cart_data

    def save(self, commit=True):
        order = super().save(commit=False)

        price = 0.00
        for product in self.products:
            price += float(product.price) * int(self.cart_data[str(product.id)])

        order.price = price

        if commit:
            order.save()

            # create OrderProduct instances
            for product in self.products:
                OrderProduct.objects.create(
                    order=order,
                    product=product,
                    quantity=int(self.cart_data[str(product.id)])
                )

            return order

        return order
