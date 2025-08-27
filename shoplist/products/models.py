from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class Product(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS = 'electronics', _('Электроника')
        COMPUTERS = 'computers', _('Компьютеры')
        APPLIANCES = 'appliances', _('Бытовая техника')
        HOME_GARDEN = 'home_garden', _('Дом и дача')
        KIDS = 'kids', _('Детские товары')
        CLOTHING = 'clothing', _('Одежда и обувь')
        BEAUTY_HEALTH = 'beauty_health', _('Красота и здоровье')
        SPORTS = 'sports', _('Спорт')
        CONSTRUCTION = 'construction', _('Строительство и ремонт')
        PETS = 'pets', _('Товары для животных')

    class PromoType(models.TextChoices):
        NONE = "none", _("Без промо")
        SEASON = "season", _("Сезонная скидка")
        SALE = "sale", _("Акция")
        SPECIAL = "special", _("Спецпредложение")

    name = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'), blank=True)
    image = models.ImageField(_('Изображение'), upload_to='products/', blank=True, null=True)
    price = models.DecimalField(_('Цена от'), max_digits=10, decimal_places=2)
    shop_addresses = models.JSONField(_('Адреса магазинов'), default=list, blank=True)
    category = models.CharField(_('Категория'), max_length=50, choices=Category.choices, default=Category.ELECTRONICS)
    promo_type = models.CharField(_("Тип промо"), max_length=20, choices=PromoType.choices, default=PromoType.NONE)
    sales_executive = models.ForeignKey(User, verbose_name=_('Менеджер'), on_delete=models.SET_NULL, null=True, blank=True)
    is_featured = models.BooleanField(
        _("Показывать в карусели"),
        default=False,
        help_text="Отметьте, если товар должен отображаться в карусели (акции, скидки и т.д.)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")
        default_permissions = ()
        permissions = [
            ("add_product", _("Может добавить товар")),
            ("change_product", _("Может изменять товар")),
            ("delete_product", _("Может удалять товар")),
            ("view_product", _("Может просматривать товар")),
        ]

    def __str__(self):
        return self.name