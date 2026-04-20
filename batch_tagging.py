import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Tag, Product

# Standards
t_special  = Tag.objects.get(name='Special')
t_uncommon = Tag.objects.get(name='Uncommon')
t_offer    = Tag.objects.get(name='Offer')
t_tested   = Tag.objects.get(name='Tested')
t_new      = Tag.objects.get(name='New')

# Tagging groups
Product.objects.filter(name__icontains='ধান').update(is_special=True)
for p in Product.objects.filter(name__icontains='ধান'):
    p.product_tags.add(t_tested, t_special)

Product.objects.filter(name__icontains='ভুট্টা').update(is_special=True)
for p in Product.objects.filter(name__icontains='ভুট্টা'):
    p.product_tags.add(t_special, t_uncommon)

Product.objects.filter(name__icontains='বাঁধাকপি').update(is_special=False)
for p in Product.objects.filter(name__icontains='বাঁধাকপি'):
    p.product_tags.add(t_new)

Product.objects.filter(name__icontains='তরমুজ').update(is_special=True)
for p in Product.objects.filter(name__icontains='তরমুজ'):
    p.product_tags.add(t_offer, t_uncommon)

Product.objects.filter(name__icontains='পেঁপে').update(is_special=True)
for p in Product.objects.filter(name__icontains='পেঁপে'):
    p.product_tags.add(t_special, t_tested)

Product.objects.filter(name__icontains='গাজর').update(is_special=False)
for p in Product.objects.filter(name__icontains='গাজর'):
    p.product_tags.add(t_new)

print("Batch tagging completed for all core product types.")
