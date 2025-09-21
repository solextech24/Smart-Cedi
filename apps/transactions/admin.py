from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model"""
    
    list_display = [
        'name', 'type', 'user', 'color_preview', 'icon', 
        'is_active', 'transaction_count', 'created_at'
    ]
    list_filter = ['type', 'is_active', 'created_at', 'user']
    search_fields = ['name', 'description', 'user__email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'type', 'description', 'user')
        }),
        ('Display Settings', {
            'fields': ('color', 'icon')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def color_preview(self, obj):
        """Display color as a colored box"""
        return format_html(
            '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #ccc;"></div>',
            obj.color
        )
    color_preview.short_description = 'Color'
    
    def transaction_count(self, obj):
        """Show number of transactions in this category"""
        return obj.transactions.count()
    transaction_count.short_description = 'Transactions'


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin interface for Transaction model"""
    
    list_display = [
        'description', 'amount_display', 'type', 'category', 
        'payment_method', 'date', 'user', 'created_at'
    ]
    list_filter = [
        'type', 'payment_method', 'date', 'is_recurring', 
        'category__type', 'user', 'created_at'
    ]
    search_fields = [
        'description', 'notes', 'reference_number', 
        'user__email', 'category__name'
    ]
    readonly_fields = ['created_at', 'updated_at', 'currency_display']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Transaction Details', {
            'fields': ('user', 'type', 'amount', 'currency_display', 'description')
        }),
        ('Categorization', {
            'fields': ('category',)
        }),
        ('Payment Information', {
            'fields': ('payment_method', 'reference_number', 'date')
        }),
        ('Additional Details', {
            'fields': ('notes', 'location', 'receipt_image', 'is_recurring')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def amount_display(self, obj):
        """Display formatted amount with currency"""
        color = 'green' if obj.type == 'income' else 'red' if obj.type == 'expense' else 'blue'
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.currency_display
        )
    amount_display.short_description = 'Amount (GHS)'
    amount_display.admin_order_field = 'amount'
    
    def get_queryset(self, request):
        """Optimize queries by selecting related objects"""
        return super().get_queryset(request).select_related('user', 'category')
