from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage.html/', views.homepage, name='homepage'),
    path('tax-calculator/', views.tax_calculator, name='tax_calculator'),
    path('simple-budget/', views.simple_budget_view, name='simple_budget'),
    path('advanced-budget/', views.advanced_budget_view, name='advanced_budget'),
    path('delete-income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),

    path('', include('register.urls')),
]