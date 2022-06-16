from multiprocessing import context
from operator import sub
from cv2 import cartToPolar
from django.shortcuts import render
from django.views.generic import TemplateView
from numpy import product
from .models import *

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_name'] = "MarkPage2k1"
        context['product_list'] = Product.objects.all().order_by("-id")
        return context

class AllProductView(TemplateView):
    template_name = 'all_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        product.view_count += 1
        product.save()
        context['product'] = product

        return context

class AddToCartView(TemplateView):
    template_name = 'add_to_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get product id from requested id
        product_id = self.kwargs['pro_id']
        # get product
        product_obj = Product.objects.get(id=product_id)


        # check if cart exits
        # del self.request.session['cart_id']
        cart_id = self.request.session.get('cart_id', None)
        
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)

            # items already exists in cart
            if this_product_in_cart.exists():
                cart_product = this_product_in_cart.last()
                cart_product.quantity += 1
                cart_product.subtotal += product_obj.selling_price
                cart_product.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()

            # new items is added in cart
            else:
                cart_product = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id

            cart_product = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save() 

        return context


class MyCartView(TemplateView):
    template_name = 'my_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'