from django.db import models

class Planning(models.Model):
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    goals = models.TextField()  # Stores the selected goals as a comma-separated string
    
    # Age fields for each goal
    age_car = models.IntegerField(blank=True, null=True)
    age_marriage = models.IntegerField(blank=True, null=True)
    age_kids = models.IntegerField(blank=True, null=True)
    age_luxury_house = models.IntegerField(blank=True, null=True)
    age_villa = models.IntegerField(blank=True, null=True)
    age_luxury_car = models.IntegerField(blank=True, null=True)
    age_education = models.IntegerField(blank=True, null=True)
    age_vacation = models.IntegerField(blank=True, null=True)
    age_retirement = models.IntegerField(blank=True, null=True)
    age_emergency_fund = models.IntegerField(blank=True, null=True)
    age_home_renovation = models.IntegerField(blank=True, null=True)
    age_business = models.IntegerField(blank=True, null=True)
    age_medical = models.IntegerField(blank=True, null=True)
    age_charity = models.IntegerField(blank=True, null=True)
    age_investment = models.IntegerField(blank=True, null=True)
    
    # Amount fields for each goal
    amount_car = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_marriage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_kids = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_luxury_house = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_villa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_luxury_car = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_education = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_vacation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_retirement = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_emergency_fund = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_home_renovation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_business = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_medical = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_charity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_investment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Planning {self.pk}"

from django.db import models

class Investment(models.Model):
    RISK_CHOICES = [
        ('conservative', 'Conservative'),
        ('moderate', 'Moderate'),
        ('aggressive', 'Aggressive'),
    ]

    risk_tolerance = models.CharField(max_length=12, choices=RISK_CHOICES)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)

