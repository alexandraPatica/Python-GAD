from django import template

register = template.Library()


@register.filter(name='cart_number')
def get_cart_items_number(session):
    return len(session.get('cart', {}).keys())


@register.filter(name='product_cart_qty')
def get_product_cart_qty(session, product_id):
    cart_data = session.get('cart', {})

    if str(product_id) in cart_data:
        return int(cart_data[str(product_id)])

    return 0


@register.filter(name='total_price')
def get_total_price(price, qty):
    return price * qty
