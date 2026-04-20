import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Product, Tag

def add_demo_tags():
    tags_to_create = [
        ('Special', 'bg-teal-600'),      # সেরা পণ্য (sera bij)
        ('Uncommon', 'bg-red-600'),      # আনকমন
        ('Offer', 'bg-orange-600'),      # অফার
        ('Tested', 'bg-green-600'),      # পরিক্ষিত
        ('New', 'bg-green-700'),         # নতুন পণ্য
    ]

    tag_objects = {}
    for name, color in tags_to_create:
        tag, _ = Tag.objects.get_or_create(name=name, defaults={'color': color})
        tag_objects[name] = tag

    products = list(Product.objects.all())
    
    for i, p in enumerate(products):
        p.product_tags.clear()
        
        # Adding exactly the ones user asked for, grouped so they look great on UI
        if i % 3 == 0:
            p.product_tags.add(tag_objects['New'], tag_objects['Special'], tag_objects['Offer'])
        elif i % 3 == 1:
            p.product_tags.add(tag_objects['Tested'], tag_objects['Uncommon'])
        else:
            p.product_tags.add(tag_objects['Offer'], tag_objects['New'], tag_objects['Tested'])

    print("Success: New tags (notun, offer, sera bij, uncommon, porikkhito) explicitly added to all demo products.")

if __name__ == "__main__":
    add_demo_tags()
