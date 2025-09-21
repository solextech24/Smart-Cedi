from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from decimal import Decimal
from datetime import datetime
from apps.transactions.models import Category, Transaction

User = get_user_model()


class Budget(models.Model):
    """
    Budget model for setting spending limits on categories
    Supports monthly, weekly, and custom period budgets
    """
    PERIOD_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
        ('custom', 'Custom Period'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
        ('exceeded', 'Exceeded'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='budgets',
        help_text="User who owns this budget"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='budgets',
        help_text="Category this budget applies to"
    )
    name = models.CharField(
        max_length=200,
        help_text="Budget name (e.g., 'Monthly Food Budget')"
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Budget limit amount in Ghana Cedis (GHS)"
    )
    period = models.CharField(
        max_length=20,
        choices=PERIOD_CHOICES,
        default='monthly',
        help_text="Budget period type"
    )
    start_date = models.DateField(
        help_text="When this budget period starts"
    )
    end_date = models.DateField(
        help_text="When this budget period ends"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text="Current status of this budget"
    )
    alert_percentage = models.IntegerField(
        default=80,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Send alert when spending reaches this percentage of budget"
    )
    description = models.TextField(
        blank=True,
        help_text="Optional description of budget goals or notes"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this budget is currently active"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'category', 'start_date', 'end_date']
        ordering = ['-start_date', 'category__name']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['start_date', 'end_date']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__lt=models.F('end_date')),
                name='budget_valid_date_range'
            ),
        ]

    def __str__(self):
        return f"{self.name} - GHS {self.amount} ({self.period})"

    @property
    def currency_display(self):
        """Returns formatted budget amount with currency"""
        return f"GHS {self.amount:,.2f}"

    @property
    def spent_amount(self):
        """Calculate total spent in this budget's category during the budget period"""
        spent = Transaction.objects.filter(
            user=self.user,
            category=self.category,
            type='expense',
            date__gte=self.start_date,
            date__lte=self.end_date
        ).aggregate(total=models.Sum('amount'))['total'] or Decimal('0.00')
        
        return spent

    @property
    def remaining_amount(self):
        """Calculate remaining budget amount"""
        return self.amount - self.spent_amount

    @property
    def percentage_used(self):
        """Calculate percentage of budget used"""
        if self.amount > 0:
            return min((self.spent_amount / self.amount * 100), 100)
        return 0

    @property
    def is_over_budget(self):
        """Check if budget has been exceeded"""
        return self.spent_amount > self.amount

    @property
    def should_alert(self):
        """Check if alert should be triggered based on alert percentage"""
        return self.percentage_used >= self.alert_percentage

    @property
    def days_remaining(self):
        """Calculate days remaining in budget period"""
        today = timezone.now().date()
        if today > self.end_date:
            return 0
        return (self.end_date - today).days

    @property
    def is_current(self):
        """Check if budget is currently active (within date range)"""
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    def save(self, *args, **kwargs):
        """
        Custom save method to validate dates and update status
        """
        # Validate dates
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date")
        
        # Get original status if this is an existing record
        original_status = None
        if self.pk:
            try:
                original_status = Budget.objects.get(pk=self.pk).status
            except Budget.DoesNotExist:
                pass
        
        # Auto-update status only for new objects or when user hasn't changed status
        should_auto_update = (self.pk is None) or (original_status is not None and self.status == original_status)
        
        if should_auto_update:
            if self.is_active and self.is_current:
                if self.is_over_budget:
                    self.status = 'exceeded'
                else:
                    self.status = 'active'
            elif timezone.now().date() > self.end_date:
                self.status = 'completed'
        
        super().save(*args, **kwargs)


class BudgetAlert(models.Model):
    """
    Model to track budget alerts and notifications
    """
    ALERT_TYPES = [
        ('threshold', 'Threshold Reached'),
        ('exceeded', 'Budget Exceeded'),
        ('daily_reminder', 'Daily Reminder'),
        ('weekly_summary', 'Weekly Summary'),
    ]

    budget = models.ForeignKey(
        Budget,
        on_delete=models.CASCADE,
        related_name='alerts',
        help_text="Budget this alert relates to"
    )
    alert_type = models.CharField(
        max_length=20,
        choices=ALERT_TYPES,
        help_text="Type of alert"
    )
    message = models.TextField(
        help_text="Alert message content"
    )
    percentage_at_alert = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Budget percentage when alert was triggered"
    )
    is_read = models.BooleanField(
        default=False,
        help_text="Whether user has read this alert"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.budget.name} - {self.get_alert_type_display()}"
