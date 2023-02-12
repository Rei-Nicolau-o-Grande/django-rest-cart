from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)

from .views import ListProduct, CartApi, item_cart_delete, item_cart_post


urlpatterns = [

    path('products', ListProduct.as_view(), name='list_products'),
    path('cart', CartApi.as_view({'get': 'list'}), name='cart'),
    path('cart/item/', item_cart_post, name='item-cart-post'),
    path('cart/item/<pk>', item_cart_delete, name='item-cart-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]