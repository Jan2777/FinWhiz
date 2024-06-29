from django import forms
from .models import Planning, Investment

class PlanningForm(forms.Form):
    age = forms.CharField(label='Your Age', max_length=100, required=False)
    salary = forms.CharField(label='Your Salary', max_length=100, required=False)
    goals = forms.MultipleChoiceField(
        label='Select Goals',
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('car', 'Car'),
            ('marriage', 'Marriage'),
            ('kids', 'Kids'),
            ('luxury_house', 'Luxury House'),
            ('villa', 'Villa'),
            ('luxury_car', 'Luxury Car'),
            ('education', 'Education'),
            ('vacation', 'Vacation'),
            ('retirement', 'Retirement'),
            ('emergency_fund', 'Emergency Fund'),
            ('home_renovation', 'Home Renovation'),
            ('business', 'Business'),
            ('medical', 'Medical'),
            ('charity', 'Charity'),
            ('investment', 'Investment'),
        ],
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for choice in self.fields['goals'].choices:
            self.fields[f'age_{choice[0]}'] = forms.IntegerField(
                label=f'Expected Age for {choice[1]}',
                required=False,
                widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'display:none;'})
            )
            self.fields[f'amount_{choice[0]}'] = forms.DecimalField(
                label=f'Expected Amount for {choice[1]}',
                required=False,
                widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'display:none;'})
            )

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('risk_tolerance', 'investment_amount')
        labels = {
            'risk_tolerance': 'Risk Tolerance',
            'investment_amount': 'Investment Amount'
        }
        widgets = {
            'risk_tolerance': forms.Select(choices=[
                ('conservative', 'Conservative'),
                ('moderate', 'Moderate'),
                ('aggressive', 'Aggressive')
            ]),
            # Correct the widget for investment_amount
            'investment_amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
