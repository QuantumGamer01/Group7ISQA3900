"""
URL configuration for Group7Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from Group7Budgeting import views
from Group7Budgeting.views import IncomeEntryListView, IncomeEntryCreateView, IncomeEntryUpdateView, \
    IncomeEntryDeleteView, IncomeEntryDetailView, AllIncomeEntriesView

#from Group7Project.register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
    settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}), #serve static files when deployed
    path('', views.homepage, name='homepage'),
    path('homepage.html', views.homepage, name='homepage'),
    path('tax-calculator/', views.tax_calculator, name='tax_calculator'),
    path('simple-budget/', views.simple_budget_view, name='simple_budget'),
    path('advanced-budget/', views.advanced_budget, name='advanced_budget'),
    path('delete-income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('register.urls')),
    path('income-entries/', IncomeEntryListView.as_view(), name='income_entry_list'),
    path('income-entry/create/', IncomeEntryCreateView.as_view(), name='income_entry_create'),
    path('income-entry/<int:pk>/update/', IncomeEntryUpdateView.as_view(), name='income_entry_update'),
    path('income-entry/<int:pk>/delete/', IncomeEntryDeleteView.as_view(), name='income_entry_delete'),
    path('income-entry/<int:pk>/', IncomeEntryDetailView.as_view(), name='income_entry_detail'),
    path('all-income-entries/', AllIncomeEntriesView.as_view(), name='all_income_entries'),
    path('users/', views.user_list, name='user_list'),

]