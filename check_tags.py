import os
import django
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Product
from api.serializers import ProductSerializer

def check():
    products = list(Product.objects.all())
    print("Total products:", len(products))
    if not products: return
        
    data = ProductSerializer(products, many=True).data
    print(json.dumps([{'name': d['name'][:10], 'tags': d['tags']} for d in data[:5]], ensure_ascii=False, indent=2))

if __name__ == '__main__':
    check()
