from django.urls import path, include
from . import views
from django.urls import include

from .views import IncomeEntryListView, IncomeEntryCreateView, IncomeEntryUpdateView, IncomeEntryDeleteView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage.html/', views.homepage, name='homepage'),
    path('tax-calculator/', views.tax_calculator, name='tax_calculator'),
    path('simple-budget/', views.simple_budget_view, name='simple_budget'),
    path('advanced-budget/', views.advanced_budget, name='advanced_budget'),
    path('delete-income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('', include('register.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('income-entries/', IncomeEntryListView.as_view(), name='income_entry_list'),
    path('income-entry/create/', IncomeEntryCreateView.as_view(), name='income_entry_create'),
    path('income-entry/<int:pk>/update/', IncomeEntryUpdateView.as_view(), name='income_entry_update'),
    path('income-entry/<int:pk>/delete/', IncomeEntryDeleteView.as_view(), name='income_entry_delete'),
]