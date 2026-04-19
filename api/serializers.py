from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Article, ContactMessage


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
        
        # Create an automatic account if it doesn't exist
        phone = validated_data.get('phone')
        from django.contrib.auth.models import User
        if phone and not User.objects.filter(username=phone).exists():
            User.objects.create_user(username=phone, password=phone)

        # Create the order first
        order = Order.objects.create(**validated_data)
        
        subtotal = 0
        total_weight = 0
        for item_data in items_data:
            product_id = item_data.get('product')
            quantity = item_data.get('quantity', 1)
            try:
                product = Product.objects.get(id=product_id)
                
                # STOCK CONTROL LOGIC
                if product.stock_quantity < quantity:
                    raise serializers.ValidationError(
                        f"ক্ষমা করবেন, {product.name} এর পর্যপ্ত স্টক নেই। বর্তমানে মাত্র {product.stock_quantity} টি স্টকে আছে।"
                    )
                
                # Decrement stock
                product.stock_quantity -= quantity
                if product.stock_quantity == 0:
                    product.in_stock = False
                product.save()

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
                pass

        import math
        if order.delivery_zone == 'Dhaka City':
            base_charge = 70
        elif order.delivery_zone == 'Dhaka Suburb':
            base_charge = 100
        else:
            base_charge = 120

        extra_weight = max(0, total_weight - 0.5)
        extra_charge = math.ceil(extra_weight) * 10
        
        if total_weight >= 5:
            delivery_charge = 0
        else:
            delivery_charge = base_charge + extra_charge
            
        total_price = subtotal + delivery_charge

        order.subtotal = subtotal
        order.delivery_charge = delivery_charge
        order.total_price = total_price
        order.save()
        return order

class PublicOrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity']

class PublicOrderSerializer(serializers.ModelSerializer):
    items = PublicOrderItemSerializer(many=True, read_only=True)
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'total_price', 'created_at', 'items']

    def get_customer_name(self, obj):
        # Mask name for privacy, e.g., "Rahim Mia" -> "Rahim***"
        name = obj.name or "একজন গ্রাহক"
        parts = name.split()
        if len(parts) > 1:
            return parts[0] + " সাহেব"
        return name[:3] + "***"


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

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
