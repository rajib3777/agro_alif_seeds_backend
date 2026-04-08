import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Category, Product

Category.objects.all().delete()
Product.objects.all().delete()

c_dhan  = Category.objects.create(name="ধান")
c_gom   = Category.objects.create(name="গম")
c_vutta = Category.objects.create(name="ভুট্টা")
c_sobji = Category.objects.create(name="সবজি")
c_fol   = Category.objects.create(name="ফল")

products = [
    # (category, name, description, price, image_path, is_special)
    (c_dhan,  "উফশী বোরো ধান (BRRI 28)",    "উচ্চ ফলনশীল বোরো ধান, প্রতি বিঘায় ২৮-৩০ মণ ফলন।",          150.00, "/seed_rice.png",  False),
    (c_dhan,  "ব্রি ধান ৮৯",                 "দীর্ঘস্থায়ী, রোগ প্রতিরোধী উফশী আমন ধান।",                  160.00, "/seed_rice.png",  False),
    (c_vutta, "সর্গাম সুদান ঘাস বীজ",       "গবাদিপশুর জন্য উচ্চ পুষ্টিকর ঘাস। দ্রুত বর্ধনশীল।",        300.00, "/sorghum.jpg",    True),
    (c_vutta, "প্যাসিফিক ৯৮ হাইব্রিড ভুট্টা","উচ্চ ফলনশীল হাইব্রিড ভুট্টা, সারা বছর চাষযোগ্য।",          250.00, "/seed_corn.png",  False),
    (c_vutta, "সুপার শাইন ভুট্টা",           "মিষ্টি ও কোমল হাইব্রিড ভুট্টা বীজ।",                         280.00, "/seed_corn.png",  False),
    (c_sobji, "হাইব্রিড বাঁধাকপি বীজ",      "শীতকালীন বাঁধাকপি, ১.৫-২ কেজি পর্যন্ত ফলন হয়।",              50.00, "/seed_veg.png",   False),
    (c_sobji, "উন্নত জাতের গাজর",            "গাঢ় লাল রঙের গাজর, ভিটামিন এ সমৃদ্ধ।",                       120.00, "/seed_veg.png",   False),
    (c_sobji, "টমেটো সুরমা হাইব্রিড",       "রোগ প্রতিরোধী হাইব্রিড টমেটো, দীর্ঘদিন ফলন দেয়।",           80.00, "/seed_veg.png",   False),
    (c_gom,   "সোনালিকা গম",                "উচ্চ প্রোটিন সমৃদ্ধ গমের বীজ, খরা সহনশীল জাত।",              200.00, "/seed_wheat.png", False),
    (c_gom,   "শতাব্দী গম",                "বাংলাদেশের আবহাওয়ায় উপযুক্ত, উচ্চ ফলনশীল গম।",              180.00, "/seed_wheat.png", False),
    (c_fol,   "হাইব্রিড পেঁপে (Red Lady)", "মিষ্টি ও উচ্চ ফলনশীল পেঁপে বীজ, ৯০ দিনে ফলন দেয়।",         800.00, "/seed_veg.png",   False),
    (c_sobji, "উচ্চ ফলনশীল লম্বা লঙ্কা",  "অত্যন্ত ঝাল ও দীর্ঘস্থায়ী লঙ্কা বীজ।",                       100.00, "/seed_veg.png",   False),
    (c_fol,   "হাইব্রিড তরমুজ",            "বড় আকারের মিষ্টি তরমুজ, কালো ডোরাকাটা।",                    1500.00, "/seed_rice.png",  False),
]

for c, n, d, p, img, sp in products:
    Product.objects.create(category=c, name=n, description=d, price=p, image=img, in_stock=True, is_special=sp)

print(f"Created {len(products)} products successfully.")
