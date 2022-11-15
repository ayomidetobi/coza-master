from django.urls import path
from . import views
from .views import index,about,product,home_02,product_detail,home_03,shoping_cart,contact,blog_details,blog,remove_from_cart,remove_single_item_from_cart,AddCouponView,add_to_cart,Checkout,signup,RequestRefundView,PaymentView

app_name = 'cloth'

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('about', about.as_view(), name="about"),
    path('contact', contact.as_view(), name="contact"),
    path('home_03', home_03.as_view(), name="home-03"),
    path('home_02', home_02.as_view(), name="home-02"),
    path('product', product.as_view(), name="product"),
    path('product/<slug>/', product_detail.as_view(), name="product-detail"),
    path('blog', blog.as_view(), name="blog"),
    path('accounts/signup', views.signup, name="signup"),
    path('shoping_cart', shoping_cart.as_view(), name="shoping-cart"),
    path('blog_detail', blog_details.as_view(), name="blog-detail"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('checkout', Checkout.as_view(), name="checkout"),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')


]