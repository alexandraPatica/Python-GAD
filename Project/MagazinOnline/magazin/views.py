from django.shortcuts import render, Http404, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from magazin.models import Products
from magazin.forms import AddProductForm, FilterProducts, OrderForm


# Create your views here.
def homepage(request):
    print(type(render))
    return render(request, 'homepage.html', {
        "name": "DJANGO"
    })


def products(request):
    print(type(render))

    form = FilterProducts(request.GET)
    if form.is_valid():
        products = form.get_products()
    else:
        products = Products.objects.all()

    paginator = Paginator(products, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    return render(request, 'products.html', {
        'page_obj': page_obj,
        'form': form
    })


def add_product(request):
    if request.method == 'GET':
        form = AddProductForm()
        return render(request, 'add_product.html', {
            'form': form
        })
    if request.method == 'POST':
        print(request.POST)

        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, f'Product added!')

            return redirect(reverse('products:view_all'))

        return render(request, 'add_product.html', {
            'form': form
        })

    raise Http404('Method not allowed')


def add_product_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        qty = request.POST.get('quantity', '1')

        try:
            qty = int(qty)

            # if product.quantity < qty:
            #     messages.error(request, 'Unavailable stock!')
            #     return redirect(reverse('products:view_all'))
        except ValueError:
            raise Http404('Quantity must be a number.')

        if 'cart' not in request.session:
            request.session['cart'] = {}

        # request.session['cart'][str(product_id)] = str(qty)
        # existing_qty = request.session['cart'].get(str(product_id), '0')
        # existing_qty = int(existing_qty)
        request.session['cart'] = {
            **request.session['cart'],
            # str(product_id): str(existing_qty + qty),
            str(product_id): str(qty),
        }

        return redirect(reverse('products:view_all'))

    raise Http404('Method not allowed!')


def view_cart(request):
    cart_data = request.session.get('cart', {})
    products = Products.objects.filter(id__in=[int(p_id) for p_id in cart_data.keys()])

    if request.method == 'GET':
        form = OrderForm(products, cart_data)
    else:
        form = OrderForm(products, cart_data, request.POST)

        if form.is_valid():
            form.save()

            request.session['cart'] = {}
            messages.success(request, 'Order was successfully created.')
            return redirect(reverse('products:view_all'))

    return render(request, 'cart.html', {
        'products': products,
        'form': form,
    })
