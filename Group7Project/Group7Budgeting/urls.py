from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage.html/', views.homepage, name='homepage'),
    path('tax-calculator/', views.tax_calculator, name='tax_calculator'),
    path('simple-budget/', views.simple_budget_view, name='simple_budget'),
    path('advanced-budget/', views.advanced_budget_view, name='advanced_budget'),
    path('', include('register.urls')),
]