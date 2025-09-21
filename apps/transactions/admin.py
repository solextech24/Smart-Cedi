from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
import re
from .models import Category, Transaction


def sanitize_color(color_value):
    """
    Sanitize color value to prevent XSS and ensure safe CSS color format
    Returns a safe color value or fallback if validation fails
    """
    if not color_value:
        return '#000000'  # Fallback for empty/None values
    
    # Normalize the input
    normalized_color = str(color_value).strip().lower()
    
    # Define safe hex color patterns
    hex_6_pattern = r'^#[0-9a-f]{6}$'  # #RRGGBB
    hex_3_pattern = r'^#[0-9a-f]{3}$'  # #RGB
    
    # Define allowlist of safe CSS color names
    safe_css_colors = {
        'black', 'white', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta',
        'orange', 'purple', 'pink', 'brown', 'gray', 'grey', 'lime', 'navy',
        'olive', 'silver', 'teal', 'aqua', 'maroon', 'fuchsia'
    }
    
    # Validate against hex patterns
    if re.match(hex_6_pattern, normalized_color) or re.match(hex_3_pattern, normalized_color):
        return normalized_color
    
    # Validate against safe CSS color names
    if normalized_color in safe_css_colors:
        return normalized_color
    
    # If validation fails, return safe fallback
    return '#000000'


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
        """Display color as a colored box with XSS protection"""
        # Sanitize the color value to prevent XSS
        safe_color = sanitize_color(obj.color)
        
        return format_html(
            '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #ccc;" title="{}"></div>',
            safe_color,
            escape(obj.color)  # Show original value in tooltip, properly escaped
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
