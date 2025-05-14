from django.shortcuts import render, redirect, get_object_or_404

from .forms import ExpenseEntryForm, IncomeEntryForm
from .models import IncomeCategory, ExpenseCategory, IncomeEntry, ExpenseEntry, AdvancedBudget


# Create your views here.
def tax_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            income = float(request.POST.get('income'))
            tax_rate = float(request.POST.get('tax_rate'))
            result = round(income * (tax_rate / 100), 2)
        except (ValueError, TypeError):
            result = "Invalid input"

    return render(request, 'Group7Budgeting/tax_calculator.html', {'result': result})

def simple_budget_view(request):
    return render(request, 'simple_budget.html')

def advanced_budget_view(request):
    populate_default_categories()

    if request.method == 'POST':
        if 'add_income' in request.POST:
            income_form = IncomeEntryForm(request.POST)
            if income_form.is_valid():
                income_form.save()
                return redirect('advanced_budget')
        elif 'add_expense' in request.POST:
            expense_form = ExpenseEntryForm(request.POST)
            if expense_form.is_valid():
                expense_form.save()
                return redirect('advanced_budget')
    else:
        income_form = IncomeEntryForm()
        expense_form = ExpenseEntryForm()

    expenses = ExpenseEntry.objects.all()

    incomes = IncomeEntry.objects.all()
    total_income = sum([income.amount for income in incomes])
    total_expense = sum([expense.amount for expense in expenses])
    remaining = total_income - total_expense

    return render(request, 'advanced_budget.html', {
        'income_form': income_form,
        'expense_form': expense_form,
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'remaining': remaining
    })



def homepage(request):
    return render(request, 'homepage.html', )

def advanced_budget(request):
    if request.method == 'POST':
        category = request.POST['category']
        assigned = request.POST['assigned']
        activity = request.POST['activity']
        available = request.POST['available']

        new_budget = AdvancedBudget(
            Advanced_budget_name=category,
            income_category=category,
            expense_category=None,
            amount=assigned,
        )
        new_budget.save()

        return redirect('advanced_budget')

    else:
        form = AdvancedBudgetForm()

    budgets = AdvancedBudget.objects.all()

    return render(request, 'advanced_budget.html', {'form': form, 'budgets': budgets})

def populate_default_categories():
    default_income = ['Salary', 'Investments', 'Other Income']
    default_expense = ['Rent', 'Gas', 'Groceries', 'Utilities', 'Dining', 'Emergency Fund']

    for name in default_income:
        IncomeCategory.objects.get_or_create(Inccategory_name=name)

    for name in default_expense:
        ExpenseCategory.objects.get_or_create(Expcategory_name=name)

def delete_budget(request, budget_id):
    budget = get_object_or_404(AdvancedBudget, pk=budget_id)
    budget.delete()
    return redirect('advanced_budget')

def delete_income(request, income_id):
    income = get_object_or_404(IncomeEntry, id=income_id)
    income.delete()
    return redirect('advanced_budget')

def delete_expense(request, expense_id):
    expense = get_object_or_404(ExpenseEntry, id=expense_id)
    expense.delete()
    return redirect('advanced_budget')

