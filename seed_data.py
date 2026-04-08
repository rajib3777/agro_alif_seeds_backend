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

    Product.objects.create(
        category=c_dhan, name="উফশী বোরো ধান (BRRI Dhan 28)", description="উচ্চ ফলনশীল বোরো ধান। দ্রুত বর্ধনশীল এবং রোগ প্রতিরোধ ক্ষমতা সম্পন্ন। প্রতি একরে ফলন সন্তোষজনক।", price=150.00, in_stock=True,
        image="https://images.unsplash.com/photo-1595841696677-6489ff3f8cd1?auto=format&fit=crop&w=600"
    )
    
    Product.objects.create(
        category=c_dhan, name="ব্রি ধান ৮৯", description="দীর্ঘস্থায়ী এবং উচ্চ পুষ্টির বোরো ধান।", price=160.00, in_stock=True,
        image="https://images.unsplash.com/photo-1586208559648-93f5451525a7?auto=format&fit=crop&w=600"
    )

    Product.objects.create(
        category=c_vutta, name="সর্গাম সুদান ঘাস বীজ (Sorghum Sudan)", description="উচ্চ ফলনশীল গবাদিপশুর পুষ্টিকর ঘাস। এটি খরা সহনশীল এবং দ্রুত বৃদ্ধি পায়।", price=300.00, in_stock=True, is_special=True,
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Sorghum_grains.jpg/640px-Sorghum_grains.jpg"
    )

    Product.objects.create(
        category=c_vutta, name="প্যাসিফিক ৯৮ ভুট্টা", description="উচ্চ ফলনশীল হাইব্রিড ভুট্টা।", price=250.00, in_stock=True,
        image="https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=600"
    )
    
    Product.objects.create(
        category=c_vutta, name="সুপার শাইন ভুট্টা", description="মিষ্টি হাইব্রিড ভুট্টা বীজ। গবাদিপশুর খাদ্য ও মানুষের খাওয়ার উপযোগী।", price=280.00, in_stock=True,
        image="https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=600"
    )

    Product.objects.create(
        category=c_sobji, name="হাইব্রিড বাঁধাকপি", description="শীতকালীন উচ্চ ফলনশীল হাইব্রিড জাতের বাঁধাকপি বীজ।", price=50.00, in_stock=True,
        image="https://images.unsplash.com/photo-1512621843614-b3e18997428f?auto=format&fit=crop&w=600"
    )
    
    Product.objects.create(
        category=c_sobji, name="উন্নত জাতের গাজর", description="স্বাস্থ্যকর গাজর বীজ। সঠিক পরিপক্বতা এবং চমৎকার রং।", price=120.00, in_stock=True,
        image="https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=600"
    )

    Product.objects.create(
        category=c_sobji, name="টমেটো সুরমা", description="হাইব্রিড টমেটো বীজ। সারাবছর ফলনের জন্য ভালো।", price=80.00, in_stock=True,
        image="https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=600"
    )

    Product.objects.create(
        category=c_gom, name="সোনালিকা গম", description="উচ্চ মাত্রার প্রোটিন সমৃদ্ধ গমের বীজ। পোকা মাকড় প্রতিরোধী।", price=200.00, in_stock=True,
        image="https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=600"
    )

if __name__ == '__main__':
    seed()
    print("Seed data created successfully.")
