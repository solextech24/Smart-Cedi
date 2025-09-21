from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'  # Full path for our nested structure
    
    def ready(self):
        """Import signals when the app is ready"""
        import apps.accounts.signals
