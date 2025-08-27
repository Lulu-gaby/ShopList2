from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from .mixins import SalesExecutiveRequiredMixin

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset().order_by('-created_at')

        # Поиск
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

        # Категория
        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category)

        return qs


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(SalesExecutiveRequiredMixin, CreateView):
    template_name = 'products/product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class ProductUpdateView(SalesExecutiveRequiredMixin, UpdateView):
    template_name = 'products/product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteView(SalesExecutiveRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('product_list')
