import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Tag, Product

# Standard tags mapping to Tailwind colors (matching screenshot look)
tags_data = [
    ('TwelveMonth', 'bg-blue-500'),  # ১২ মাস
    ('Tested', 'bg-green-500'),      # পরিক্ষিত
    ('Special', 'bg-teal-500'),      # সেরা পণ্য
    ('Uncommon', 'bg-red-500'),      # আনকমন
    ('Offer', 'bg-orange-500'),     # অফার
    ('Popular', 'bg-green-700'),     # পপুলার
    ('New', 'bg-green-600'),         # নতুন পণ্য
]

for name, color in tags_data:
    Tag.objects.update_or_create(name=name, defaults={'color': color})

print("Standard Screenshot Tags bootstrapped successfully.")

# Apply some diverse tags and cashback to first 5 products for preview
products = Product.objects.all()[:10]
t_12m = Tag.objects.get(name='TwelveMonth')
t_test = Tag.objects.get(name='Tested')
t_unco = Tag.objects.get(name='Uncommon')
t_special = Tag.objects.get(name='Special')
t_offer = Tag.objects.get(name='Offer')
t_pop = Tag.objects.get(name='Popular')

import random

for p in products:
    p.product_tags.clear()
    p.product_tags.add(t_12m) # Most seeds are 12m
    
    # Randomly add 2-3 more tags
    extra_tags = [t_test, t_unco, t_special, t_offer, t_pop]
    selection = random.sample(extra_tags, 3)
    p.product_tags.add(*selection)
    
    # Add some cashback
    p.cashback_amount = random.choice([3, 4, 5, 10])
    p.save()

print("Initial data populated with tags and cashback.")
