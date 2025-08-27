from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('sales_executive', 'Менеджер'),
        ('customer', 'Покупатель'),
    )

    email = models.EmailField(unique=True, verbose_name="Email",  error_messages={"unique": "Пользователь с таким email уже существует."})
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer', verbose_name='Роль пользователя')

    @property
    def is_sales_executive(self):
        return self.role == 'sales_executive' or self.role == 'admin'

    @property
    def is_customer(self):
        return self.role == 'customer'

    @property
    def is_admin(self):
        return self.role == 'admin'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"