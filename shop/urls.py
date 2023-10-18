from django.urls import path
from .views import ProductViewSet, OrderViewSet

urlpatterns = [
    path('products-list/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('product-create/', ProductViewSet.as_view({'post': 'create'}), name='product-create'),
    path('product-detail/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
    path('products/<int:pk>/update/', ProductViewSet.as_view({'put': 'update'}), name='product-update'),
    path('products/<int:pk>/delete/', ProductViewSet.as_view({'delete': 'destroy'}), name='product-delete'),
    path('orders-list/', OrderViewSet.as_view({'get': 'list'}), name='order-list'),
    path('orders/create/', OrderViewSet.as_view({'post': 'create'}), name='order-create'),
    # path('orders/<int:pk>/update/', OrderViewSet.as_view({'put': 'update'}), name='order-update'),
    path('orders/<int:pk>/cancel/', OrderViewSet.as_view({'delete': 'destroy'}), name='order-cancel'),
]
