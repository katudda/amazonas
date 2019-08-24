from django.urls import path
from apps.api.views import CategoryListView, ProductListView, ProductDetailListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='api-categories-list'),
    path('products/', ProductListView.as_view(), name='api-product-list'),
    path('products/<int:pk>', ProductDetailListView.as_view(), name='api-product-detail'),
]