from django.contrib import admin
from .models import Product
from .forms import ProductForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = (
        "name",
        "category",
        "price",
        "promo_type",
        "is_featured",
        "created_at",
    )
    list_filter = ("category", "promo_type", "is_featured")
    search_fields = ("name", "description")
    list_editable = ("is_featured",)

    fieldsets = (
        (None, {
            "fields": ("name", "description", "image", "price", "shop_addresses_raw")
        }),
        ("Категория и промо", {
            "fields": ("category", "promo_type", "is_featured")
        }),
        ("Прочее", {
            "fields": ("sales_executive",)
        }),
    )