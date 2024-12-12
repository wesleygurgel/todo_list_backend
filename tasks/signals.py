from django.db.models.signals import pre_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(pre_migrate)
def create_default_user(sender, **kwargs):
    """Cria um usuário padrão antes de carregar as fixtures."""
    if not User.objects.filter(username='default_user').exists():
        User.objects.create_user(
            username='admin',
            password='admin',
            email='default@example.com'
        )
        print("Usuário padrão criado: username='admin', password='admin'")
