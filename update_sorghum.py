import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from api.models import Product

p = Product.objects.filter(is_special=True).first()
if p:
    p.image = '/sorghum.png'
    p.save()
    print("Sorghum updated")
