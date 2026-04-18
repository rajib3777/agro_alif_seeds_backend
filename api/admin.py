from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Article, ContactMessage

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total_price', 'status_label', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'address')
    inlines = [OrderItemInline]
    readonly_fields = ('subtotal', 'delivery_charge', 'total_price', 'created_at')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        response.write(u'\ufeff'.encode('utf8')) # BOM for Excel
        writer = csv.writer(response)
        
        writer.writerow(['Order ID', 'Name', 'Phone', 'Address', 'Subtotal', 'Delivery Charge', 'Total Price', 'Status', 'Date'])
        
        for obj in queryset:
            writer.writerow([
                obj.id, 
                obj.name, 
                obj.phone, 
                obj.address, 
                obj.subtotal, 
                obj.delivery_charge, 
                obj.total_price, 
                obj.status, 
                obj.created_at.strftime("%Y-%m-%d %H:%M")
            ])
            
        return response
    
    export_as_csv.short_description = "নির্বাচিত অর্ডারগুলো CSV আকারে ইনপুট নিন"
    
    fieldsets = (
        ("গ্রাহকের তথ্য", {
            "fields": ("name", "phone", "address", "delivery_zone")
        }),
        ("অর্থপ্রদান সংক্রান্ত", {
            "fields": ("subtotal", "delivery_charge", "total_price")
        }),
        ("অবস্থা", {
            "fields": ("status", "created_at")
        }),
    )

    def status_label(self, obj):
        from django.utils.html import format_html
        colors = {
            'Pending': 'orange',
            'Processing': 'blue',
            'Shipped': 'purple',
            'Delivered': 'green',
            'Cancelled': 'red',
        }
        color = colors.get(obj.status, 'gray')
        return format_html(
            '<span style="background: {}; color: white; padding: 2px 8px; border-radius: 10px; font-weight: bold; font-size: 10px;">{}</span>',
            color, obj.status
        )
    status_label.short_description = "অবস্থা"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'in_stock_label', 'is_special')
    list_filter = ('category', 'in_stock', 'is_special')
    search_fields = ('name', 'description')
    list_editable = ('in_stock', 'is_special')

    def in_stock_label(self, obj):
        return "✅ ইন স্টক" if obj.in_stock else "❌ স্টক আউট"
    in_stock_label.short_description = "স্টক অবস্থা"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone', 'message')
    readonly_fields = ('name', 'phone', 'message', 'created_at')
