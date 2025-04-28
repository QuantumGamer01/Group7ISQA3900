from django import forms
from .models import IncomeEntry, ExpenseEntry

class IncomeEntryForm(forms.ModelForm):
    class Meta:
        model = IncomeEntry
        fields = ['category', 'amount']

class ExpenseEntryForm(forms.ModelForm):
    class Meta:
        model = ExpenseEntry
        fields = ['category', 'amount']
