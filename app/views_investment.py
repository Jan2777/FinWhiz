import requests
from django.shortcuts import render
from .forms import InvestmentForm
from .models import Investment
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

RISK_TOLERANCE_MAP = {
    'conservative': 1,
    'moderate': 2,
    'aggressive': 3
}

# Mock function to get market data
def get_market_data():
    # Replace this with actual API call
    # response = requests.get('https://api.example.com/market-data')
    # data = response.json()
    data = {
        'suggestions': [
            {'name': 'Low-Risk Bonds', 'details': 'Safe investments with moderate returns.'},
            {'name': 'Index Funds', 'details': 'Good for moderate risk tolerance and diversified portfolio.'},
            {'name': 'High-Risk Stocks', 'details': 'Higher potential returns with higher risks.'}
        ]
    }
    return data

def investment_view(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            # Save form data to Investment model
            investment = form.save()

            # Mock data processing and prediction
            risk_tolerance = investment.risk_tolerance
            investment_amount = float(investment.investment_amount)  # Convert Decimal to float

            # Convert risk tolerance to numerical value
            risk_tolerance_value = RISK_TOLERANCE_MAP.get(risk_tolerance, 2)  # Default to 'moderate' if not found

            data = {'risk_tolerance': [risk_tolerance_value], 'investment_amount': [investment_amount]}
            df = pd.DataFrame(data)

            # Example model training (replace with your actual model training logic)
            X = df[['risk_tolerance']]
            y = df['investment_amount'] * 1.5  # Example: Mock target

            # Since we only have one sample, we can't split the data into training and testing sets
            # Instead, we'll use the entire dataset to train the model
            model = RandomForestRegressor()
            model.fit(X, y)

            # Make a prediction based on the user's input
            input_data = [[risk_tolerance_value]]
            prediction = model.predict(input_data)

            # Get market data and suggestions
            market_data = get_market_data()

            # Prepare context to pass to result.html
            context = {
                'investment': investment,
                'prediction': prediction[0] if prediction else 'N/A',
                'suggestions': market_data['suggestions']
            }
            return render(request, 'investment/result.html', context)
    else:
        form = InvestmentForm()

    # Render index.html with the form for GET requests or if form is invalid
    return render(request, 'investment/index.html', {'form': form})

def result(request):
    return render(request, 'investment/result.html')
