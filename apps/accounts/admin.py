from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    """Inline admin for UserProfile to show with User"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = (
        ('monthly_income', 'currency'),
        ('phone_number', 'date_of_birth', 'timezone'),
        ('date_format', 'budget_alerts', 'email_notifications'),
        ('ai_recommendations_enabled', 'risk_tolerance'),
        'financial_goals',
        'avatar',
    )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User admin with UserProfile inline"""
    inlines = (UserProfileInline,)
    
    # Customize the user list display
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    
    # Customize the user form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    
    ordering = ('email',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin for UserProfile model"""
    list_display = ('user', 'currency', 'monthly_income', 'ai_recommendations_enabled', 'created_at')
    list_filter = ('currency', 'ai_recommendations_enabled', 'risk_tolerance', 'created_at')
    search_fields = ('user__email', 'user__username', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Financial Information'), {
            'fields': ('monthly_income', 'currency')
        }),
        (_('Personal Information'), {
            'fields': ('phone_number', 'date_of_birth', 'timezone', 'avatar')
        }),
        (_('Preferences'), {
            'fields': ('date_format', 'budget_alerts', 'email_notifications')
        }),
        (_('AI Settings'), {
            'fields': ('ai_recommendations_enabled', 'risk_tolerance', 'financial_goals')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
