from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from apps.catalogs.models import Product, Comment
from apps.catalogs.forms import CommentForm


def products_list(request):
    products = Product.objects.filter(
        published_at__isnull=False
    ).order_by('description')
    return render(
        request, 'catalogs/products_list.html', {'products': products}
    )


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalogs/product_detail.html', {'product': product})


def add_comment_to_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = CommentForm()
    return render(request, 'catalogs/add_comment_to_product.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('product_detail', pk=comment.product.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('product_detail', pk=comment.product.pk)