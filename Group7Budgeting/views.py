from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExpenseEntryForm, IncomeEntryForm
from .models import IncomeCategory, ExpenseCategory, IncomeEntry, ExpenseEntry, AdvancedBudget, PremExpense, PremIncome, User


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



def homepage(request):
    return render(request, 'homepage.html', )
@login_required
def advanced_budget(request):
    # Fetch user-specific data
    incomes = IncomeEntry.objects.filter(user=request.user)
    expenses = ExpenseEntry.objects.filter(user=request.user)

    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    remaining = total_income - total_expense

    if request.method == 'POST':
        if 'add_income' in request.POST:  # Handle the income form submission
            income_form = IncomeEntryForm(request.POST)
            if income_form.is_valid():
                income_entry = income_form.save(commit=False)  # Don't save to the database yet
                income_entry.user = request.user  # Assign the currently logged-in user
                income_entry.save()  # Now save to the database
                return redirect('advanced_budget')  # Reload the page after submission
        elif 'add_expense' in request.POST:  # Handle the expense form submission
            expense_form = ExpenseEntryForm(request.POST)
            if expense_form.is_valid():
                expense_entry = expense_form.save(commit=False)  # Don't save to the database yet
                expense_entry.user = request.user  # Assign the currently logged-in user
                expense_entry.save()  # Now save to the database
                return redirect('advanced_budget')  # Reload the page after submission
    else:
        income_form = IncomeEntryForm()  # Empty form for adding income
        expense_form = ExpenseEntryForm()  # Empty form for adding expenses

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'remaining': remaining,
        'income_form': income_form,
        'expense_form': expense_form,
    }
    return render(request, 'advanced_budget.html', context)



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
    income = get_object_or_404(IncomeEntry, id=income_id, user=request.user)  # Check ownership
    if income.user != request.user:
        return HttpResponseForbidden("You are not authorized to delete this income.")
    income.delete()
    return redirect('advanced_budget')


def delete_expense(request, expense_id):
    expense = get_object_or_404(ExpenseEntry, id=expense_id, user=request.user)
    if expense.user != request.user:
        return HttpResponseForbidden("You are not authorized to delete this expense")
    expense.delete()
    return redirect('advanced_budget')

class AdvancedBudgetByUserListView(LoginRequiredMixin, ListView):
    model = AdvancedBudget
    template_name = "advanced_budget.html"
    paginate_by = 10

    def get_queryset(self):
        return IncomeEntry.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incomes = PremIncome.objects.filter(user=self.request.user)
        expenses = PremExpense.objects.filter(user=self.request.user)

        context["total_income"] = incomes.aggregate(Sum("amount"))["amount__sum"] or 0
        context["total_expense"] = expenses.aggregate(Sum("amount"))["amount__sum"] or 0
        context["remaining"] = context["total_income"] - context["total_expense"]
        context["incomes"] = incomes
        context["expenses"] = expenses
        return context

class IncomeEntryListView(ListView):
    model = IncomeEntry
    template_name = 'income_entry/income_entry_list.html'
    context_object_name = 'incomeentry_list'

class IncomeEntryCreateView(CreateView):
    model = IncomeEntry
    fields = ['category', 'amount']
    template_name = 'income_entry/income_entry_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeEntryUpdateView(UpdateView):
    model = IncomeEntry
    fields = ['user', 'category', 'amount']
    template_name = 'income_entry/income_entry_form.html'

class IncomeEntryDeleteView(DeleteView):
    model = IncomeEntry
    success_url = reverse_lazy('income_entry_list')
    template_name = 'income_entry/income_entry_confirm_delete.html'

class IncomeEntryDetailView(DetailView):
    model = IncomeEntry
    template_name = 'income_entry/income_entry_detail.html'
    context_object_name = 'income_entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_entries'] = IncomeEntry.objects.all()  # ✅ Add this
        return context

class AllIncomeEntriesView(TemplateView):
    template_name = 'income_entry/all_income_entries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_entries'] = IncomeEntry.objects.all()
        return context

def superuser_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)


@superuser_required
def user_list(request):
    if request.method == "POST":
        # Handle user deletion
        user_id = request.POST.get("delete_user")
        user_to_delete = get_object_or_404(User, id=user_id)

        # Prevent superuser from deleting themselves
        if user_to_delete == request.user:
            return render(request, "user_list.html", {
                "users": User.objects.all(),
                "error": "You cannot delete yourself!"
            })

        user_to_delete.delete()
        return redirect("user_list")

    # Render the list of users
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})
