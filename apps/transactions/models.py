from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
import re

User = get_user_model()


def validate_hex_color(value):
    """
    Validator function to ensure color field contains a valid hex color code
    Format: #RRGGBB where RR, GG, BB are hexadecimal digits
    """
    hex_color_pattern = r'^#[0-9A-Fa-f]{6}$'
    if not re.match(hex_color_pattern, value):
        raise ValidationError(
            f'"{value}" is not a valid hex color code. '
            'Use format #RRGGBB (e.g., #FF5733, #007BFF)'
        )


class Category(models.Model):
    """
    Category model for organizing transactions
    Supports both income and expense categories
    """
    CATEGORY_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    name = models.CharField(
        max_length=100,
        help_text="Category name (e.g., 'Food', 'Salary', 'Transport')"
    )
    type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPES,
        help_text="Whether this category is for income or expenses"
    )
    description = models.TextField(
        blank=True,
        help_text="Optional description of what this category covers"
    )
    color = models.CharField(
        max_length=7,
        default='#007bff',
        validators=[validate_hex_color],
        help_text="Hex color code for UI display (e.g., #FF5733)"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Icon name for UI display (e.g., 'food', 'transport')"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories',
        help_text="User who owns this category"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this category is currently in use"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ['name', 'user', 'type']
        ordering = ['type', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Transaction(models.Model):
    """
    Transaction model for recording all financial activities
    Supports both income and expense transactions in Ghana Cedis
    """
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer'),
    ]
    
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('mobile_money', 'Mobile Money'),
        ('bank_transfer', 'Bank Transfer'),
        ('card', 'Debit/Credit Card'),
        ('cheque', 'Cheque'),
        ('online', 'Online Payment'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions',
        help_text="User who made this transaction"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transactions',
        help_text="Category this transaction belongs to"
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Transaction amount in Ghana Cedis (GHS)"
    )
    type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        help_text="Type of transaction"
    )
    description = models.CharField(
        max_length=255,
        help_text="Brief description of the transaction"
    )
    notes = models.TextField(
        blank=True,
        help_text="Additional notes or details about the transaction"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        default='cash',
        help_text="How the payment was made"
    )
    reference_number = models.CharField(
        max_length=100,
        blank=True,
        help_text="Transaction reference (mobile money ref, bank ref, etc.)"
    )
    date = models.DateField(
        help_text="Date when the transaction occurred"
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        help_text="Where the transaction took place"
    )
    receipt_image = models.ImageField(
        upload_to='receipts/%Y/%m/',
        blank=True,
        null=True,
        help_text="Photo of receipt or proof of transaction"
    )
    is_recurring = models.BooleanField(
        default=False,
        help_text="Whether this is a recurring transaction"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['user', 'date']),
            models.Index(fields=['user', 'type']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.description} - GHS {self.amount} ({self.date})"

    @property
    def currency_display(self):
        """Returns formatted amount with currency"""
        return f"GHS {self.amount:,.2f}"

    def save(self, *args, **kwargs):
        """
        Custom save method to ensure category type matches transaction type
        """
        if self.category and self.type in ['income', 'expense']:
            if self.category.type != self.type:
                raise ValueError(
                    f"Transaction type '{self.type}' doesn't match "
                    f"category type '{self.category.type}'"
                )
        super().save(*args, **kwargs)
