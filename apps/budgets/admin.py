from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import Budget, BudgetAlert


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    """Admin interface for Budget model"""
    
    list_display = [
        'name', 'amount_display', 'category', 'period', 'progress_bar',
        'status', 'start_date', 'end_date', 'user'
    ]
    list_filter = [
        'status', 'period', 'is_active', 'start_date', 
        'category__type', 'user', 'created_at'
    ]
    search_fields = [
        'name', 'description', 'user__email', 'category__name'
    ]
    readonly_fields = [
        'created_at', 'updated_at', 'currency_display', 
        'spent_amount', 'remaining_amount', 'percentage_used',
        'days_remaining', 'is_current'
    ]
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Budget Information', {
            'fields': ('name', 'user', 'category', 'amount', 'currency_display')
        }),
        ('Period Settings', {
            'fields': ('period', 'start_date', 'end_date')
        }),
        ('Status & Alerts', {
            'fields': ('status', 'alert_percentage', 'is_active')
        }),
        ('Budget Progress', {
            'fields': ('spent_amount', 'remaining_amount', 'percentage_used', 'days_remaining', 'is_current'),
            'classes': ('collapse',)
        }),
        ('Additional Details', {
            'fields': ('description',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def amount_display(self, obj):
        """Display formatted budget amount"""
        return format_html(
            '<span style="font-weight: bold;">{}</span>',
            obj.currency_display
        )
    amount_display.short_description = 'Budget Amount'
    amount_display.admin_order_field = 'amount'
    
    def progress_bar(self, obj):
        """Display budget progress as a progress bar"""
        # Use original percentage for color decision (not capped)
        color = 'red' if obj.percentage_used > 100 else 'orange' if obj.percentage_used > obj.alert_percentage else 'green'
        
        # Cap percentage for display width and label
        display_percentage = min(obj.percentage_used, 100)
        
        return format_html(
            '<div style="width: 100px; background-color: #f0f0f0; border-radius: 3px;">'
            '<div style="width: {}%; background-color: {}; height: 20px; border-radius: 3px; text-align: center; color: white; font-size: 12px; line-height: 20px;">'
            '{:.1f}%'
            '</div></div>',
            display_percentage, color, obj.percentage_used  # Show actual percentage in label
        )
    progress_bar.short_description = 'Progress'
    
    def get_queryset(self, request):
        """Optimize queries by selecting related objects"""
        return super().get_queryset(request).select_related('user', 'category')


@admin.register(BudgetAlert)
class BudgetAlertAdmin(admin.ModelAdmin):
    """Admin interface for BudgetAlert model"""
    
    list_display = [
        'budget', 'alert_type', 'percentage_display', 
        'is_read', 'created_at'
    ]
    list_filter = [
        'alert_type', 'is_read', 'created_at', 
        'budget__user', 'budget__category'
    ]
    search_fields = [
        'budget__name', 'message', 'budget__user__email'
    ]
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Alert Information', {
            'fields': ('budget', 'alert_type', 'message')
        }),
        ('Alert Details', {
            'fields': ('percentage_at_alert', 'is_read')
        }),
        ('Timestamp', {
            'fields': ('created_at',)
        }),
    )
    
    def percentage_display(self, obj):
        """Display percentage with formatting"""
        return f"{obj.percentage_at_alert:.1f}%"
    percentage_display.short_description = 'Budget %'
    percentage_display.admin_order_field = 'percentage_at_alert'
    
    def get_queryset(self, request):
        """Optimize queries by selecting related objects"""
        return super().get_queryset(request).select_related('budget', 'budget__user', 'budget__category')
