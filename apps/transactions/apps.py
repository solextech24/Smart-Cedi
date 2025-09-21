from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.transactions'
    verbose_name = 'Transactions'
    
    def ready(self):
        """Import signals when app is ready"""
        try:
            import apps.transactions.signals
        except ImportError:
            pass
