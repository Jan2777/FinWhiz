import requests
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from django.shortcuts import render
from .forms import PlanningForm, InvestmentForm
from .models import Planning

def home(request):
    return render(request, 'FinWhiz/index.html')

from django.shortcuts import render
from .forms import PlanningForm
from .models import Planning

def index(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']
            selected_goals = form.cleaned_data['goals']
            
            ages = {}
            amounts = {}
            for goal in selected_goals:
                ages[goal] = form.cleaned_data[f'age_{goal}']
                amounts[goal] = form.cleaned_data[f'amount_{goal}']

            # Perform any processing or calculations here
            # For simplicity, just display the selected goals and their inputs
            context = {
                'age': age,
                'salary': salary,
                'selected_goals': selected_goals,
                'ages': ages,
                'amounts': amounts,
            }
            return render(request, 'planning/result.html', context)
    else:
        form = PlanningForm()

    return render(request, 'planning/index.html', {'form': form})

def result(request):
    return render(request, 'planning/result.html')


import requests
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from django.shortcuts import render
from .forms import InvestmentForm
from .models import Investment

# views.py
from django.shortcuts import render
from .forms import InvestmentForm
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from decimal import Decimal

def investment_view(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            # Save form data to Investment model
            investment = form.save()
            
            # Mock data processing and prediction
            risk_tolerance = investment.risk_tolerance
            investment_amount = float(investment.investment_amount)  # Convert Decimal to float
            
            data = {'risk_tolerance': [risk_tolerance], 'investment_amount': [investment_amount]}
            df = pd.DataFrame(data)
            
            # Example model training (replace with your actual model training logic)
            X = df[['risk_tolerance']]
            y = df['investment_amount'] * 1.5  # Example: Mock target
            
            # Since we only have one sample, we can't split the data into training and testing sets
            # Instead, we'll use the entire dataset to train the model
            model = RandomForestRegressor()
            model.fit(X, y)
            
            # Make a prediction based on the user's input
            input_data = [[investment.risk_tolerance]]
            prediction = model.predict(input_data)
            
            # Prepare context to pass to result.html
            context = {
                'investment': investment,
                'prediction': prediction[0] if prediction else 'N/A'
            }
            return render(request, 'investment/result.html', context)
    else:
        form = InvestmentForm()
    
    # Render index.html with the form for GET requests or if form is invalid
    return render(request, 'investment/index.html', {'form': form})

def result(request):
    return render(request, 'investment/result.html')