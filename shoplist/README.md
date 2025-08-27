# ShopList

**ShopList** — минималистичная витрина товаров с информацией о магазинах, реализованная на Django. Пользователи могут просматривать товары, а менеджеры (sales\_executive) и администраторы управлять ими через удобный веб-интерфейс.

---

## 🔹 Функционал

### Для всех пользователей

* Регистрация и вход в систему.
* Просмотр списка товаров с миниатюрой, названием и ценой.
* Поиск товаров по названию.
* Просмотр детальной информации о товаре, включая описание, цену и адреса магазинов.

### Для sales\_executive

* Добавление новых товаров (с изображением, ценой, адресами магазинов).
* Редактирование и удаление своих товаров через интерфейс на детальной странице товара.
* Панель управления товарами через ссылки “Редактировать” / “Удалить”.

### Для admin

* Полный доступ ко всем товарам и пользователям через Django admin.
* Возможность изменять, добавлять и удалять любые товары.

---

## 🔹 Структура проекта

```
shoplist/
│
├─ shoplist/            # Корневые настройки Django
│   ├─ settings.py
│   ├─ urls.py
│   ├─ wsgi.py
│   ├─ asgi.py
│
├─ accounts/            # Пользователи и роли
│   ├─ models.py        # Пользователь с ролями: admin, sales_executive, customer
│   ├─ forms.py         # Форма регистрации
│   ├─ views.py
│   ├─ urls.py
│   ├─ admin.py
│   └─ migrations/      # Миграции приложения
│
├─ products/            # Товары
│   ├─ models.py        # Модель Product с sales_executive
│   ├─ forms.py
│   ├─ views.py
│   ├─ urls.py
│   ├─ admin.py
│   ├─ mixins.py        # SalesExecutiveRequiredMixin
│   └─ migrations/      # Миграции приложения
│
├─ core/                # Дополнения
│   └─ management/commands/translate_permissions.py
│
├─ templates/           # Шаблоны
│   ├─ base.html
│   ├─ index.html
│   ├─ accounts/
│   └─ products/
│
├─ static/              # CSS, изображения
├─ media/               # Загруженные изображения товаров
├─ db.sqlite3           # База данных SQLite
├─ manage.py
└─ README.md
```

---

## 🔹 Установка и запуск

1. **Клонируйте репозиторий**

```bash
git clone <repo_url>
cd shoplist
```

2. **Создайте и активируйте виртуальное окружение**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Установите зависимости**

```bash
pip install -r requirements.txt
```

> Если используете `.env` для `SECRET_KEY`, убедитесь, что установлен `python-dotenv`.

4. **Примените миграции**

```bash
python manage.py migrate
```

5. **Создайте суперпользователя (admin)**

```bash
python manage.py createsuperuser
```

6. **Переведите права доступа на русский (опционально)**

```bash
python manage.py translate_permissions
```

7. **Запустите сервер**

```bash
python manage.py runserver
```

8. **Откройте проект**
   Перейдите в браузере на [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔹 Стек технологий

* Python 3.10+
* Django 5.2.5 (совместимо с 4.x)
* SQLite
* Django Templates + Bootstrap 5.3.3
* Адаптивный дизайн для мобильных и десктопов

---

## 🔹 Модели

### User (accounts/models.py)

* `username`, `email`, `password`
* `role`: `admin`, `sales_executive`, `customer`
* Свойства для проверки роли: `is_admin`, `is_sales_executive`, `is_customer`

### Product (products/models.py)

* `name`, `description`, `image`, `price`, `category`, `promo_type`
* `shop_addresses` — список адресов магазинов
* `sales_executive` — менеджер, создавший товар
* `is_featured` — отображать в карусели
* `created_at` — дата создания

---

## 🔹 Авторизация и роли

| Роль                 | Доступ                                                           |
| -------------------- | ---------------------------------------------------------------- |
| **Customer**         | Просмотр товаров                                                 |
| **Sales\_executive** | Добавление, редактирование, удаление своих товаров               |
| **Admin**            | Полный доступ ко всем товарам и пользователям через Django admin |

---

## 🔹 Дополнительно

* Медиа-файлы хранятся в папке `media/`.
* Статические файлы (CSS, изображения) — в `static/`.
* Настроен адаптивный дизайн через Bootstrap.
* Реализована карусель промо и отображение новых товаров на главной странице.
