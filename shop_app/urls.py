from urllib.parse import urlparse
from django.urls import path
from .views import *

app_name = 'shop_app'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("all-products/", AllProductView.as_view(), name="all_products"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),

    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("my-cart/", MyCartView.as_view(), name="my_cart"),
    path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name="manage_cart"),
    path('empty-cart/', EmptyCartView.as_view(), name="empty_cart"),

    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('register/', CustomerRegistrationView.as_view(), name="customer_registration"),
    path('logout/', CustomerLogoutView.as_view(), name="customer_logout"),
    path('login/', CustomerLoginView.as_view(), name="customer_login"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="passwordforgot"),

    path("profile/", CustomerProfileView.as_view(), name="customer_profile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customer_order_detail"),

    path("search/", SearchView.as_view(), name="search"),


    #admin site
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),     
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(), name="adminorderdetail"),

    path('admin-all-orders/', AdminOrderListView.as_view(), name="adminorderlist"),
    path('admin-order-<int:pk>-change/', AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),
    path("admin-products/list/", AdminProductListView.as_view(), name="adminproductlist"),
    path("admin-product/add/", AdminProductCreateView.as_view(), name="adminproductcreate"),
    
]
