from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import User
from .forms import RegisterForm
from products.models import Product


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # --- Карусель акций ---
        promo_types = Product.PromoType.choices
        carousel_items = []
        for code, name in promo_types:
            if code == "none":
                continue
            product_for_image = Product.objects.filter(promo_type=code).first()
            if product_for_image:
                carousel_items.append({
                    "promo_type": code,
                    "promo_name": name,
                    "image_url": product_for_image.image.url if product_for_image.image else None,
                    "link": reverse('product_list') + f'?promo={code}'
                })
        context['carousel_items'] = carousel_items

        # --- Последние товары ---
        context['new_products'] = Product.objects.all().order_by('-created_at')[:10]

        # --- Категории для "Каталога" ---
        context['categories'] = Product.Category.choices

        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = reverse_lazy('login')

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        user.role = 'customer'
        user.save(update_fields=['role'])
        self.object = user
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))