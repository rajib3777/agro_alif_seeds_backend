from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="ক্যাটাগরির নাম")
    icon = models.ImageField(upload_to='categories/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="পণ্যের নাম")
    description = models.TextField(verbose_name="বিবরণ")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="মূল্য (৳)")
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    in_stock = models.BooleanField(default=True, verbose_name="স্টকে আছে")
    is_special = models.BooleanField(default=False, verbose_name="বিশেষ পণ্য")

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name="গ্রাহকের নাম")
    phone = models.CharField(max_length=20, verbose_name="ফোন নম্বর")
    address = models.TextField(verbose_name="ঠিকানা")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="মোট মূল্য")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
