from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Handles authentication and basic user information.
    """
    email = models.EmailField(unique=True, help_text="Email address for login")
    
    # Override to make email the login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email


class UserProfile(models.Model):
    """
    Extended profile information for financial tracking and AI features.
    Separated from User model for better organization and flexibility.
    """
    CURRENCY_CHOICES = [
        ('GHS', 'Ghana Cedi'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('NGN', 'Nigerian Naira'),
    ]
    
    RISK_TOLERANCE_CHOICES = [
        ('conservative', 'Conservative'),
        ('moderate', 'Moderate'),
        ('aggressive', 'Aggressive'),
    ]
    
    DATE_FORMAT_CHOICES = [
        ('DD/MM/YYYY', 'DD/MM/YYYY'),
        ('MM/DD/YYYY', 'MM/DD/YYYY'),
        ('YYYY-MM-DD', 'YYYY-MM-DD'),
    ]
    
    # Link to User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Financial Information
    monthly_income = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Monthly income in user's currency"
    )
    currency = models.CharField(
        max_length=3, 
        choices=CURRENCY_CHOICES, 
        default='GHS',
        help_text="Primary currency for all transactions"
    )
    
    # Personal Information
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    timezone = models.CharField(max_length=50, default='Africa/Accra')
    
    # App Preferences
    date_format = models.CharField(
        max_length=10, 
        choices=DATE_FORMAT_CHOICES, 
        default='DD/MM/YYYY'
    )
    budget_alerts = models.BooleanField(
        default=True, 
        help_text="Receive alerts when approaching budget limits"
    )
    email_notifications = models.BooleanField(default=True)
    
    # AI and Investment Preferences
    ai_recommendations_enabled = models.BooleanField(
        default=True,
        help_text="Allow AI to provide financial recommendations"
    )
    risk_tolerance = models.CharField(
        max_length=20,
        choices=RISK_TOLERANCE_CHOICES,
        default='moderate',
        help_text="Investment risk tolerance for AI recommendations"
    )
    financial_goals = models.TextField(
        blank=True,
        help_text="User's financial goals for personalized advice"
    )
    
    # Profile Image
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"{self.user.email} Profile"
    
    @property
    def display_name(self):
        """Return user's full name or email if name not available"""
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.email
    
    def get_currency_symbol(self):
        """Return currency symbol for display"""
        currency_symbols = {
            'GHS': '₵',
            'USD': '$',
            'EUR': '€',
            'GBP': '£',
            'NGN': '₦',
        }
        return currency_symbols.get(self.currency, self.currency)
