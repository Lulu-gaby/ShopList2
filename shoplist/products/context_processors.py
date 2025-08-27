from .models import Product

def categories_processor(request):
    categories = Product.Category.choices  # [(value, display), ...]
    return {
        'categories': categories
    }