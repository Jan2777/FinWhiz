from django.shortcuts import render
from .forms import PlanningForm
from .models import Planning
from datetime import datetime

def calculate_savings_plan(age, salary, goals, ages):
    current_year = datetime.now().year
    savings_plan = {}

    goal_amounts = {
        'car': 20000,
        'marriage': 30000,
        'kids': 50000,
        'luxury_house': 500000,
        'villa': 1000000,
        'luxury_car': 100000,
        'education': 100000,
        'vacation': 10000,
        'retirement': 200000,
        'emergency_fund': 10000,
        'home_renovation': 20000,
        'business': 50000,
        'medical': 20000,
        'charity': 5000,
        'investment': 50000
    }

    for goal in goals:
        if goal in goal_amounts:
            goal_amount = goal_amounts[goal]
            if goal in ages and ages[goal]:
                years_to_save = ages[goal] - age
            else:
                years_to_save = 10  # Default years to save if age not specified

            monthly_savings = goal_amount / (years_to_save * 12)
            savings_plan[f'monthly_{goal}_savings'] = monthly_savings

    return savings_plan

def index(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']
            goals = form.cleaned_data['goals']

            # Extract ages for selected goals
            ages = {
                'car': form.cleaned_data.get('age_car'),
                'marriage': form.cleaned_data.get('age_marriage'),
                'kids': form.cleaned_data.get('age_kids'),
                'luxury_house': form.cleaned_data.get('age_luxury_house'),
                'villa': form.cleaned_data.get('age_villa'),
                'luxury_car': form.cleaned_data.get('age_luxury_car'),
                'education': form.cleaned_data.get('age_education'),
                'vacation': form.cleaned_data.get('age_vacation'),
                'retirement': form.cleaned_data.get('age_retirement'),
                'emergency_fund': form.cleaned_data.get('age_emergency_fund'),
                'home_renovation': form.cleaned_data.get('age_home_renovation'),
                'business': form.cleaned_data.get('age_business'),
                'medical': form.cleaned_data.get('age_medical'),
                'charity': form.cleaned_data.get('age_charity'),
                'investment': form.cleaned_data.get('age_investment'),
            }

            planning = Planning.objects.create(
                age=age,
                salary=salary,
                goals=','.join(goals)  # Store goals as a comma-separated string
            )

            savings_plan = calculate_savings_plan(age, salary, goals, ages)

            context = {
                'age': age,
                'salary': salary,
                **savings_plan
            }
            return render(request, 'planning/result.html', context)
    else:
        form = PlanningForm()
    
    return render(request, 'planning/index.html', {'form': form})

def result(request):
    return render(request, 'planning/result.html')
