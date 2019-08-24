from rest_framework import serializers

from apps.catalogs.models import Category, Product


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'description',
            'final_price',
            'suggested_price',
            'image',
            'has_offer',
            'category',
            'created_at',
            'published_at',
        )

    def create(self, validated_data):
        category = validated_data.pop('category')
        instance, is_created = Category.objects.get_or_create(**category)
        return Product.objects.create(category=instance, **validated_data)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'description',
            'final_price',
            'suggested_price',
            'image',
            'has_offer',
            'category',
            'created_at',
            'published_at',
        )

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.final_price = validated_data.get('final_price', instance.final_price)
        instance.suggested_price = validated_data.get('suggested_price', instance.suggested_price)
        instance.image = validated_data.get('image', instance.image)
        instance.has_offer = validated_data.get('has_offer', instance.has_offer)
        if validated_data['category']:
            instance.category.id = validated_data.get('category', instance.category)

        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.published_at = validated_data.get('published_at', instance.published_at)
        instance.save()
        return instance