from django.urls import path, include
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('investment/', include('app.urls_investment')),
    path('planning/', include('app.urls_planning')),
    path('', views.home, name='home'),  # Route root URL to home view
]
