from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    userscreated_at = models.DateTimeField(auto_now_add=True)
    usersupdated_at = models.DateTimeField(auto_now=True)




class BasicUsers(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2)
    BUTransacCreated_at = models.DateTimeField(auto_now_add=True)
    BUTransacUpdated_at = models.DateTimeField(auto_now=True)

class IncomeCategory(models.Model):
    Inccategory_id = models.AutoField(primary_key=True)
    Inccategory_name = models.CharField(max_length=100)
    Inccategory_created = models.DateTimeField(auto_now_add=True)
    Inccategory_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Inccategory_name

class ExpenseCategory(models.Model):
    Expcategory_id = models.AutoField(primary_key=True)
    Expcategory_name = models.CharField(max_length=100)
    Expcategory_created = models.DateTimeField(auto_now_add=True)
    Expcategory_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Expcategory_name

class AdvancedBudget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Advanced_budget_id = models.AutoField(primary_key=True)
    Advanced_budget_name = models.CharField(max_length=100)
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    Advanced_budget_created = models.DateTimeField(auto_now_add=True)
    Advanced_budget_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Advanced_budget_name


class PremIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    PremIncome_id = models.AutoField(primary_key=True)
    PremIncome_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PremIncome_type = models.CharField(max_length=100)
    PremIncome_description = models.CharField(max_length=100)
    PremIncome_created = models.DateTimeField(auto_now_add=True)
    PremIncome_updated = models.DateTimeField(auto_now=True)

class PremExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    PremExpense_id = models.AutoField(primary_key=True)
    PremExpense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PremExpense_type = models.CharField(max_length=100)
    PremExpense_description = models.CharField(max_length=100)
    PremExpense_created = models.DateTimeField(auto_now_add=True)
    PremExpense_updated = models.DateTimeField(auto_now=True)

class IncomeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class ExpenseEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
