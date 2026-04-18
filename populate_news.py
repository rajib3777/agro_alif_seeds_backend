import os
import django
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Article

mock_articles = [
    {
        "title": "উন্নত মানের সর্গাম সুদান বীজ বপনের সঠিক সময় ও পদ্ধতি",
        "content": "সর্গাম সুদান একটি উচ্চ ফলনশীল ঘাস যা গবাদি পশুর জন্য অত্যন্ত পুষ্টিকর। এটি বপনের সঠিক সময় হলো চৈত্র থেকে আষাঢ় মাস পর্যন্ত। সঠিক পদ্ধতিতে চাষ করলে এটি থেকে বছরে ৫-৬ বার ঘাস কাটা সম্ভব। খামারিদের জন্য এটি একটি অত্যন্ত লাভজনক সমাধান।",
    },
    {
        "title": "আধুনিক ডেইরি খামার ব্যবস্থাপনায় নতুন দিগন্ত",
        "content": "ডেইরি খামারকে লাভজনক করতে হলে সুষম খাদ্যের পাশাপাশি কাঁচা ঘাসের কোনো বিকল্প নেই। উন্নত মানের ঘাসের বীজ ব্যবহার করে আপনি আপনার খামারের উৎপাদন প্রায় ৪০% পর্যন্ত বাড়াতে পারেন। আলিফ এগ্রো সার্ভিস দিচ্ছে খামারিদের সব ধরণের কারিগরি সহায়তা।",
    },
    {
        "title": "হাইব্রিড ভুট্টার ভালো ফলন পেতে করণীয় টিপস",
        "content": "ভুট্টা চাষে সারের সঠিক প্রয়োগ এবং আধুনিক সেচ ব্যবস্থাপনা ফলনে বড় প্রভাব ফেলে। সঠিক সময়ে আগাছা পরিষ্কার করা এবং পোকামাকড় দমন করতে পারলে ফলন কয়েকগুণ বেড়ে যায়। নিয়মিত মাঠ পর্যবেক্ষণ নিশ্চিত করুন।",
    }
]

for art in mock_articles:
    if not Article.objects.filter(title=art['title']).exists():
        Article.objects.create(
            title=art['title'],
            content=art['content']
        )
