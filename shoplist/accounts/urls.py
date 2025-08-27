from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView, ProfileView, RegisterView, logout_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', next_page='index'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]