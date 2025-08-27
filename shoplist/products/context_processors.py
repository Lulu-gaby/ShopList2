from .models import Product

def categories_processor(request):
    """
    Возвращает список всех категорий товаров для выпадающего меню Каталог.
    Используем Product.Category.choices, чтобы всегда показывались все категории на русском.
    """
    categories = Product.Category.choices  # [(value, display), ...]
    return {
        'categories': categories
    }