from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = 'Translate default auth permissions to Russian'

    def handle(self, *args, **options):
        translations = {
            # User permissions
            'add_user': 'Может добавлять пользователя',
            'change_user': 'Может изменять пользователя',
            'delete_user': 'Может удалять пользователя',
            'view_user': 'Может просматривать пользователя',
            # Group permissions
            'add_group': 'Может добавлять группу',
            'change_group': 'Может изменять группу',
            'delete_group': 'Может удалять группу',
            'view_group': 'Может просматривать группу',
            # Permission permissions
            'add_permission': 'Может добавлять право',
            'change_permission': 'Может изменять право',
            'delete_permission': 'Может удалять право',
            'view_permission': 'Может просматривать право',
            # Content type permissions
            'add_contenttype': 'Может добавлять тип содержимого',
            'change_contenttype': 'Может изменять тип содержимого',
            'delete_contenttype': 'Может удалять тип содержимого',
            'view_contenttype': 'Может просматривать тип содержимого',
            # Log entry permissions
            'add_logentry': 'Может добавлять запись журнала',
            'change_logentry': 'Может изменять запись журнала',
            'delete_logentry': 'Может удалять запись журнала',
            'view_logentry': 'Может просматривать запись журнала',
            # Session permissions (обычно нет в стандартном наборе, но для совместимости)
            'add_session': 'Может добавлять сессию',
            'change_session': 'Может изменять сессию',
            'delete_session': 'Может удалять сессию',
            'view_session': 'Может просматривать сессию',
        }

        for perm in Permission.objects.all():
            codename = perm.codename.lower()
            if codename in translations:
                perm.name = translations[codename]
                perm.save()
                self.stdout.write(self.style.SUCCESS(f'Permission "{perm.codename}" переведено на русский'))