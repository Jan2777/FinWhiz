from django.urls import path
from . import views_planning

urlpatterns = [
    path('', views_planning.index, name='planning_index'),
    path('result/', views_planning.result, name='planning_result'),
]
