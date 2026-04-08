import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Category, Product

def seed():
    Category.objects.all().delete()
    Product.objects.all().delete()

    c_dhan = Category.objects.create(name="ধান")
    c_gom = Category.objects.create(name="গম")
    c_vutta = Category.objects.create(name="ভুট্টা")
    c_sobji = Category.objects.create(name="সবজি")
    c_fol = Category.objects.create(name="ফল")

    products = [
        (c_dhan, "উফশী বোরো ধান", "উচ্চ ফলনশীল বোরো ধান।", 150.00, "/cat2.jpg", False),
        (c_dhan, "ব্রি ধান ৮৯", "দীর্ঘস্থায়ী ধান।", 160.00, "/cat3.jpg", False),
        (c_vutta, "সর্গাম সুদান ঘাস বীজ", "উচ্চ ফলনশীল গবাদিপশুর পুষ্টিকর ঘাস।", 300.00, "/sorghum.jpg", True),
        (c_vutta, "প্যাসিফিক ৯৮ ভুট্টা", "উচ্চ ফলনশীল হাইব্রিড ভুট্টা।", 250.00, "/cat1.png", False),
        (c_vutta, "সুপার শাইন ভুট্টা", "মিষ্টি হাইব্রিড ভুট্টা বীজ।", 280.00, "/cat2.jpg", False),
        (c_sobji, "হাইব্রিড বাঁধাকপি", "বাঁধাকপি বীজ।", 50.00, "/cat3.jpg", False),
        (c_sobji, "উন্নত জাতের গাজর", "স্বাস্থ্যকর গাজর বীজ।", 120.00, "/sorghum.jpg", False),
        (c_sobji, "টমেটো সুরমা", "হাইব্রিড টমেটো বীজ।", 80.00, "/cat1.png", False),
        (c_gom, "সোনালিকা গম", "উচ্চ মাত্রার প্রোটিন সমৃদ্ধ গমের বীজ।", 200.00, "/cat2.jpg", False),
        (c_fol, "হাইব্রিড পেঁপে বীজ (Red Lady)", "মিষ্টি পেঁপে বীজ, ফলন ভালো হয়।", 800.00, "/cat3.jpg", False),
        (c_sobji, "উচ্চ ফলনশীল লঙ্কা", "খুবই ঝাল লঙ্কা বীজ।", 100.00, "/cat2.jpg", False),
        (c_sobji, "শীতকালীন মুলা", "মুলা বীজ। সাদা এবং মোটা।", 60.00, "/cat1.png", False),
        (c_fol, "হাইব্রিড তরমুজ", "বড় তরমুজ। কালো খোলস।", 1500.00, "/cat3.jpg", False),
    ]

    for c, n, d, p, i, s in products:
        Product.objects.create(category=c, name=n, description=d, price=p, image=i, in_stock=True, is_special=s)

if __name__ == '__main__':
    seed()
    print("Seed data 4 created successfully.")
