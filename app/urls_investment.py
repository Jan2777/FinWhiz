# urls_investment.py

from django.urls import path
from . import views_investment

urlpatterns = [
    path('', views_investment.investment_view, name='investment_index'),
    path('result/', views_investment.result, name='investment_result'),
]
