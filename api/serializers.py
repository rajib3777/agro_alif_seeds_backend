from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        if not obj.image:
            return None
        url = str(obj.image)
        if url.startswith('http') or url.startswith('/'):
            return url
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return f'/media/{url}'


# Simple nested item input — only needs product id and quantity
class OrderItemInputSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, default=1)


class OrderSerializer(serializers.ModelSerializer):
    # Accept items as raw list but handle manually
    items = OrderItemInputSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'delivery_zone', 'subtotal', 'delivery_charge', 'total_price', 'status', 'created_at', 'items']
        read_only_fields = ['id', 'subtotal', 'delivery_charge', 'total_price', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        
        # Create the order first
        order = Order.objects.create(**validated_data)
        
        subtotal = 0
        total_weight = 0
        for item_data in items_data:
            product_id = item_data.get('product')
            quantity = item_data.get('quantity', 1)
            try:
                product = Product.objects.get(id=product_id)
                item_price = product.price * quantity
                subtotal += item_price
                total_weight += quantity
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )
            except Product.DoesNotExist:
                pass  # Skip invalid products gracefully

        import math
        if order.delivery_zone == 'Dhaka City':
            base_charge = 70
        elif order.delivery_zone == 'Dhaka Suburb':
            base_charge = 100
        else:
            base_charge = 120

        extra_weight = max(0, total_weight - 0.5)
        extra_charge = math.ceil(extra_weight) * 10
        
        delivery_charge = base_charge + extra_charge
        total_price = subtotal + delivery_charge

        order.subtotal = subtotal
        order.delivery_charge = delivery_charge
        order.total_price = total_price
        order.save()
        return order

class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_image(self, obj):
        if not obj.image:
            return None
        url = str(obj.image)
        if url.startswith('http') or url.startswith('/'):
            return url
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return f'/media/{url}'
