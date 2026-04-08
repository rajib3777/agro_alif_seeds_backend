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
        (c_dhan, "উফশী বোরো ধান (BRRI Dhan 28)", "উচ্চ ফলনশীল বোরো ধান।", 150.00, "https://images.unsplash.com/photo-1595841696677-6489ff3f8cd1?auto=format&fit=crop&w=600", False),
        (c_dhan, "ব্রি ধান ৮৯", "দীর্ঘস্থায়ী ধান।", 160.00, "https://images.unsplash.com/photo-1586208559648-93f5451525a7?auto=format&fit=crop&w=600", False),
        (c_vutta, "সর্গাম সুদান ঘাস বীজ", "উচ্চ ফলনশীল গবাদিপশুর পুষ্টিকর ঘাস।", 300.00, "https://images.unsplash.com/photo-1508061461528-ce80fff5cbcd?auto=format&fit=crop&w=600", True),
        (c_vutta, "প্যাসিফিক ৯৮ ভুট্টা", "উচ্চ ফলনশীল হাইব্রিড ভুট্টা।", 250.00, "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=600", False),
        (c_vutta, "সুপার শাইন ভুট্টা", "মিষ্টি হাইব্রিড ভুট্টা বীজ।", 280.00, "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=600", False),
        (c_sobji, "হাইব্রিড বাঁধাকপি", "বাঁধাকপি বীজ।", 50.00, "https://images.unsplash.com/photo-1512621843614-b3e18997428f?auto=format&fit=crop&w=600", False),
        (c_sobji, "উন্নত জাতের গাজর", "স্বাস্থ্যকর গাজর বীজ।", 120.00, "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=600", False),
        (c_sobji, "টমেটো সুরমা", "হাইব্রিড টমেটো বীজ।", 80.00, "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=600", False),
        (c_gom, "সোনালিকা গম", "উচ্চ মাত্রার প্রোটিন সমৃদ্ধ গমের বীজ।", 200.00, "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=600", False),
        (c_fol, "হাইব্রিড পেঁপে বীজ (Red Lady)", "মিষ্টি পেঁপে বীজ, ফলন ভালো হয়।", 800.00, "https://images.unsplash.com/photo-1517282009859-f000ef1b4408?auto=format&fit=crop&w=600", False),
        (c_sobji, "উচ্চ ফলনশীল লম্বা মরিচ", "খুবই ঝাল লঙ্কা বীজ।", 100.00, "https://images.unsplash.com/photo-1588047913501-f10f607185eb?auto=format&fit=crop&w=600", False),
        (c_sobji, "শীতকালীন মুলা", "মুলা বীজ। সাদা এবং মোটা।", 60.00, "https://images.unsplash.com/photo-1589139825442-fca19a00778c?auto=format&fit=crop&w=600", False),
        (c_fol, "হাইব্রিড তরমুজ", "বড় তরমুজ। কালো খোলস।", 1500.00, "https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?auto=format&fit=crop&w=600", False),
    ]

    for c, n, d, p, i, s in products:
        Product.objects.create(category=c, name=n, description=d, price=p, image=i, in_stock=True, is_special=s)

if __name__ == '__main__':
    seed()
    print("Seed data 2 created successfully.")
