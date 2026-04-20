import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Tag, Product, Category

# Brands
t_tested   = Tag.objects.get(name='Tested')
t_uncommon = Tag.objects.get(name='Uncommon')
t_12m      = Tag.objects.get(name='TwelveMonth')
t_special  = Tag.objects.get(name='Special')

cat_seeds = Category.objects.filter(name__icontains='বীজ').first() or Category.objects.first()

# Create fresh products for 'Tested' Section
tested_items = [
    {
        "name": "হাইব্রিড লাল শাক (পরিক্ষিত)",
        "price": 45,
        "desc": "উচ্চ ফলনশীল লাল শাকের বীজ। এটি আমাদের খামারে পরিক্ষিত এবং সেরা মানের নিশ্চয়তা।",
        "cashback": 2
    },
    {
        "name": "বারোমাসি কাঁচামরিচ (পরিক্ষিত)",
        "price": 85,
        "desc": "দেশ সেরা ঝাল মরিচের বীজ। দ্রুত ফলন দেয় এবং রোগ প্রতিরোধ ক্ষমতা বেশি।",
        "cashback": 5
    }
]

for item in tested_items:
    p, created = Product.objects.update_or_create(
        name=item['name'],
        defaults={
            'category': cat_seeds,
            'price': item['price'],
            'description': item['desc'],
            'cashback_amount': item['cashback'],
            'in_stock': True,
            'season': 'Year-round'
        }
    )
    p.product_tags.add(t_tested, t_12m, t_special)

# Create fresh products for 'Uncommon' Section
uncommon_items = [
    {
        "name": "বিদেশি ড্রাগন ফল বীজ (আনকমন)",
        "price": 250,
        "desc": "এটি একটি বিরল প্রজাতির ড্রাগন ফল। আমাদের কালেকশনের অন্যতম সেরা আনকমন পণ্য।",
        "cashback": 10
    },
    {
        "name": "ব্ল্যাক চেরি টমেটো (আনকমন)",
        "price": 120,
        "desc": "কালচে রঙের সুস্বাদু টমেটো। শৌখিন বাগানিদের জন্য এটি একটি স্পেশাল কালেকশন।",
        "cashback": 4
    }
]

for item in uncommon_items:
    p, created = Product.objects.update_or_create(
        name=item['name'],
        defaults={
            'category': cat_seeds,
            'price': item['price'],
            'description': item['desc'],
            'cashback_amount': item['cashback'],
            'in_stock': True,
            'season': 'Winter'
        }
    )
    p.product_tags.add(t_uncommon, t_12m)

print("Demo Taggable Products created successfully. Sections should be clearly visible now.")
