from django.core.management.base import BaseCommand
from ecommerce_api.models import Product

class Command(BaseCommand):
    help = 'Seeds the database with 20 shoe products'

    def handle(self, *args, **kwargs):
        shoes_data = [
            ("Air Force 1 '07", "Nike", "Lifestyle Shoes", 5495.00, 25, "US 9", "Classic white low-top leather basketball-inspired sneaker."),
            ("Dunk Low Retro", "Nike", "Lifestyle Shoes", 5895.00, 18, "US 10", "Iconic 80s hoops silhouette with crisp overlays."),
            ("Air Max 90", "Nike", "Running Shoes", 6895.00, 15, "US 9.5", "Visible Max Air cushioning with waffle outsole."),
            ("Pegasus 41", "Nike", "Running Shoes", 7395.00, 20, "US 8.5", "Responsive ReactX foam daily road running shoe."),
            ("Ultraboost Light", "Adidas", "Running Shoes", 9500.00, 12, "US 10", "Lightweight Boost midsole for maximum energy return."),
            ("Samba OG", "Adidas", "Lifestyle Shoes", 6800.00, 30, "US 8", "Timeless indoor soccer classic with gum rubber sole."),
            ("Gazelle Indoor", "Adidas", "Lifestyle Shoes", 6500.00, 14, "US 9", "Soft suede upper with translucent gum outsole."),
            ("Stan Smith", "Adidas", "Casual Shoes", 5300.00, 22, "US 9.5", "Minimalist tennis court leather sneaker."),
            ("574 Core", "New Balance", "Lifestyle Shoes", 5295.00, 28, "US 9", "Versatile everyday suede and mesh runner."),
            ("9060", "New Balance", "Lifestyle Shoes", 8995.00, 10, "US 10", "Chunky Y2K-inspired silhouette with dual-density midsole."),
            ("Fresh Foam X 1080v13", "New Balance", "Running Shoes", 9495.00, 16, "US 8.5", "Plush cushioning engineered for long-distance comfort."),
            ("Chuck Taylor All Star", "Converse", "Casual Shoes", 3490.00, 40, "US 9", "Classic high-top canvas sneaker with rubber toe cap."),
            ("Chuck 70 Vintage Canvas", "Converse", "Casual Shoes", 4490.00, 24, "US 8", "Upgraded heavy-grade canvas with glossy cream foxing."),
            ("Old Skool Classic", "Vans", "Skate Shoes", 3998.00, 35, "US 9.5", "Signature side-stripe skate shoe with waffle tread."),
            ("Sk8-Hi", "Vans", "Skate Shoes", 4498.00, 19, "US 10", "Padded high-top collar for ankle support."),
            ("Gel-Kayano 30", "ASICS", "Running Shoes", 9990.00, 11, "US 9", "4D Guidance System stability running shoe."),
            ("Gel-Nimbus 26", "ASICS", "Running Shoes", 9690.00, 14, "US 8.5", "PureGEL technology for soft landings."),
            ("Palermo Leather", "Puma", "Lifestyle Shoes", 5200.00, 21, "US 9", "80s terrace-culture low-top with signature tag."),
            ("Suede Classic XXI", "Puma", "Lifestyle Shoes", 4600.00, 27, "US 9.5", "Full suede upper with comfortable sockliner."),
            ("Cloudmonster", "On Running", "Running Shoes", 9590.00, 9, "US 10", "Max-cushioned CloudTec pods for effortless forward roll."),
        ]

        created_count = 0
        for name, brand, cat, price, stock, size, desc in shoes_data:
            _, created = Product.objects.get_or_create(
                name=name,
                brand=brand,
                defaults={
                    'category': cat,
                    'price': price,
                    'stock': stock,
                    'size': size,
                    'description': desc,
                }
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {created_count} products! Total rows: {Product.objects.count()}"))