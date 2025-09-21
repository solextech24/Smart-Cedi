from django.apps import AppConfig


class BudgetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.budgets'
    verbose_name = 'Budgets'
    
    def ready(self):
        """Import signals when app is ready"""
        try:
            import apps.budgets.signals
        except ImportError:
            pass
