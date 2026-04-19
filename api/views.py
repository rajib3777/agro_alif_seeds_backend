from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Category, Product, Order, Article, ContactMessage
from .serializers import (CategorySerializer, ProductSerializer, OrderSerializer,
                          ArticleSerializer, ContactMessageSerializer, PublicOrderSerializer)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'], url_path='restock')
    def restock(self, request, pk=None):
        product = self.get_object()
        quantity = request.data.get('quantity', 0)
        try:
            quantity = int(quantity)
            product.stock_quantity += quantity
            if product.stock_quantity > 0:
                product.in_stock = True
            product.save()
            return Response({'success': True, 'new_stock': product.stock_quantity})
        except (ValueError, TypeError):
            return Response({'error': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post', 'get']

    @action(detail=False, methods=['get'], url_path='recent')
    def recent_orders(self, request):
        recent = Order.objects.all().order_by('-created_at')[:10]
        serializer = PublicOrderSerializer(recent, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by-phone')
    def orders_by_phone(self, request):
        phone = request.query_params.get('phone', '').strip()
        if not phone:
            return Response({'error': 'Phone required'}, status=status.HTTP_400_BAD_REQUEST)
        orders = Order.objects.filter(phone=phone).order_by('-created_at')[:10]
        serializer = PublicOrderSerializer(orders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='track')
    def track_order(self, request):
        order_id = request.query_params.get('order_id', '').strip()
        phone = request.query_params.get('phone', '').strip()
        if not order_id or not phone:
            return Response({'error': 'অর্ডার আইডি এবং ফোন নম্বর দিন'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            order = Order.objects.get(id=order_id, phone=phone)
            # Use serializer for full details including items
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'অর্ডারটি খুঁজে পাওয়া যায়নি। সঠিক তথ্য দিন।'}, status=status.HTTP_404_NOT_FOUND)

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    http_method_names = ['post']


@api_view(['POST'])
def phone_login(request):
    """Login with phone number as username and password. 
    Accounts are auto-created when an order is placed using that phone number."""
    phone = request.data.get('phone', '').strip()
    password = request.data.get('password', '').strip()
    if not phone or not password:
        return Response({'error': 'ফোন নম্বর ও পাসওয়ার্ড দিন'}, status=400)
    try:
        user = User.objects.get(username=phone)
        if user.check_password(password):
            return Response({
                'success': True,
                'name': user.get_full_name() or phone,
                'phone': phone,
                'message': 'লগইন সফল হয়েছে!'
            })
        return Response({'error': 'পাসওয়ার্ড ভুল।'}, status=400)
    except User.DoesNotExist:
        return Response({'error': 'এই নম্বরে কোনো একাউন্ট নেই। আগে অর্ডার করুন বা নিবন্ধন করুন।'}, status=404)


@api_view(['POST'])
def phone_register(request):
    """Register with phone number. If the phone already has an order, 
    the account already exists — user just sets a new password."""
    phone = request.data.get('phone', '').strip()
    name = request.data.get('name', '').strip()
    password = request.data.get('password', '').strip()
    if not phone or not password or not name:
        return Response({'error': 'সব তথ্য দিন'}, status=400)
    if len(password) < 6:
        return Response({'error': 'পাসওয়ার্ড কমপক্ষে ৬ অক্ষরের হতে হবে'}, status=400)

    if User.objects.filter(username=phone).exists():
        # Account exists (from a previous order) — update name and password
        user = User.objects.get(username=phone)
        first, *rest_parts = name.split()
        user.first_name = first
        user.last_name = ' '.join(rest_parts)
        user.set_password(password)
        user.save()
        return Response({'success': True, 'name': name, 'phone': phone,
                         'message': 'একাউন্ট আপডেট হয়েছে! লগইন করুন।'})
    else:
        first, *rest_parts = name.split()
        user = User.objects.create_user(username=phone, password=password,
                                        first_name=first, last_name=' '.join(rest_parts))
        return Response({'success': True, 'name': name, 'phone': phone,
                         'message': 'একাউন্ট তৈরি হয়েছে!'})
