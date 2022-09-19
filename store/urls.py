from django.urls import path,include
from . import views
from two_factor.urls import urlpatterns as tf_urls

from store.controller import authview, cart, wishlist, checkout, order

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections" ),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>/<int:prod_id>', views.productview, name="productview"),
    
    path("product-list", views.productlistAjax),
    path("searchproduct", views.searchproduct, name="searchproduct"),
    
    path('', include(tf_urls)),
    path('register/', authview.register, name="register"),
    path('account/login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),
    path('accounts/profile/', authview.profile, name="profile"),
    
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    
    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    
    path('my-orders', order.index, name="myorders"),
    path("view-order/<str:t_no>", order.vieworder, name="orderview"),
    
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('privacy', views.privacy, name="privacy"),
    path('terms', views.terms, name="terms"),
]