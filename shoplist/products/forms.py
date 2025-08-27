from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    shop_addresses_raw = forms.CharField(
        label='Адреса магазинов (по одному в строке)',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4})
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['shop_addresses_raw'].initial = '\n'.join(
                self.instance.shop_addresses or []
            )

    def clean(self):
        cleaned = super().clean()
        raw = self.cleaned_data.get('shop_addresses_raw', '').strip()
        cleaned['shop_addresses'] = [
            line.strip() for line in raw.splitlines() if line.strip()
        ]
        return cleaned

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.shop_addresses = self.cleaned_data.get('shop_addresses', [])
        if commit:
            obj.save()
        return obj
