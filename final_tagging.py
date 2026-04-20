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
t_popular  = Tag.objects.get(name='Popular')
t_12m      = Tag.objects.get(name='TwelveMonth')
t_new      = Tag.objects.get(name='New')

# Clear existing and re-tag for a clean look
for p in Product.objects.all():
    p.product_tags.clear()
    
    # 1. Targeted tagging based on name
    name_low = p.name.lower()
    
    # Common for all
    p.product_tags.add(t_12m) 
    
    if 'ধান' in name_low or 'ভুট্টা' in name_low:
        p.product_tags.add(t_tested, t_special, t_popular)
        p.is_special = True
    elif 'সবজি' in name_low or 'বাঁধাকপি' in name_low:
        p.product_tags.add(t_new, t_tested)
    elif 'তরমুজ' in name_low or 'পেঁপে' in name_low:
        p.product_tags.add(t_uncommon, t_offer)
        p.is_special = True
    else:
        # Default for others
        p.product_tags.add(t_tested)

    p.save()

print("Comprehensive tagging completed. 'Tested' and 'Uncommon' sections should now be populated.")
