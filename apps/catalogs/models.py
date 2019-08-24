from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def _str_(self):
        return self.name

    def _str_(self):
        return self.description

class Product(models.Model):
    description = models.CharField(max_length=100)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    suggested_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="imgs/products/", null=True)
    has_offer = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    category = models.name = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)

    def _str_(self):
        return self.description
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text