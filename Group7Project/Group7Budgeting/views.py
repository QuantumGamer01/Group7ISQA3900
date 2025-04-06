from django.shortcuts import render

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
    sections = ['Needs', 'Wants', 'Savings']
    return render(request, 'advanced_budget.html', {'sections': sections})


