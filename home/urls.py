from django.urls import path
from .views import *
# from . import views


urlpatterns = [
    path('',home, name='home'),
    path('product/',product, name='product'),
    path('signup/',signup, name='signup'),


    # add to cart
    path('cart/<slug>',cart,name = 'cart'),
    path('deletecart/<slug>',deletecart,name = 'deletecart'),
    path('decreasecart/<slug>',decreasecart,name = 'decreasecart'),
    path('cart',cart,name = 'cart'),

    #contact
    path('contact/',contact,name='contact'),

    #search
    # path('search/',search,name='search'),
    path('search/',SearchView.as_view(),name='search'),

    path('shop-detail/',shop_detail,name='shop-detail'),


    # otp
    path('otp/',otp,name='otp'),


    path('test/',TestView.as_view(),name='test'),


]

 




