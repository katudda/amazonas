from django.urls import path
from apps.catalogs.views import (
    products_list,
    product_detail,
    add_comment_to_product,
    comment_approve,
    comment_remove
)

urlpatterns = [
    path('products/', products_list, name='products-list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/comment/', add_comment_to_product, name='add_comment_to_product'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
]