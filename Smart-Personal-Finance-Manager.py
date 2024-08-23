import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tkinter as tk
from tkinter import messagebox

# Expense Tracker Class
class ExpenseTracker:
    def __init__(self):
        self.expenses = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])

    def add_expense(self, date, category, description, amount):
        new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Description': [description], 'Amount': [amount]})
        self.expenses = pd.concat([self.expenses, new_expense])

    def view_expenses(self):
        return self.expenses

    def calculate_totals(self):
        daily_totals = self.expenses.resample('D', on='Date')['Amount'].sum()
        monthly_totals = self.expenses.resample('M', on='Date')['Amount'].sum()
        yearly_totals = self.expenses.resample('Y', on='Date')['Amount'].sum()
        return daily_totals, monthly_totals, yearly_totals

# Budget Management Class
class BudgetManager:
    def __init__(self):
        self.budget = 0

    def set_budget(self, budget):
        self.budget = budget

    def check_budget(self, amount):
        if amount > self.budget:
            return False
        else:
            return True

# Financial Goal Setting Class
class FinancialGoal:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def view_goals(self):
        return self.goals

# AI Assistant Class
class AIAssistant:
    def __init__(self):
        self.model = LinearRegression()

    def train_model(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def answer_query(self, query):
        # Implement NLP to answer financial queries
        tokens = word_tokenize(query)
        tokens = [t for t in tokens if t.lower() not in stopwords.words('english')]
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        # Use the trained model to answer the query
        return self.model.predict(tokens)

# GUI Class
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Smart Personal Finance Management Application")
        self.expense_tracker = ExpenseTracker()
        self.budget_manager = BudgetManager()
        self.financial_goal = FinancialGoal()
        self.ai_assistant = AIAssistant()

        # Create GUI components
        self.date_label = tk.Label(master, text="Date")
        self.date_label.pack()
        self.date_entry = tk.Entry(master)
        self.date_entry.pack()

        self.category_label = tk.Label(master, text="Category")
        self.category_label.pack()
        self.category_entry = tk.Entry(master)
        self.category_entry.pack()

        self.description_label = tk.Label(master, text="Description")
        self.description_label.pack()
        self.description_entry = tk.Entry(master)
        self.description_entry.pack()

        self.amount_label = tk.Label(master, text="Amount")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()

        self.add_expense_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack()

        self.view_expenses_button = tk.Button(master, text="View Expenses", command=self.view_expenses)
        self.view_expenses_button.pack()

        self.set_budget_button = tk.Button(master, text="Set Budget", command=self.set_budget)
        self.set_budget_button.pack()

        self.check_budget_button = tk.Button(master, text="Check Budget", command=self.check_budget)
        self.check_budget_button.pack()

        self.add_goal_button = tk.Button(master, text="Add Goal", command=self.add_goal)
        self.add_goal_button.pack()

        self.view_goals_button = tk.Button(master, text="View Goals", command=self.view_goals)
        self.view_goals_button.pack()

        self.query_label = tk.Label(master, text="Query")
        self.query_label.pack()
        self.query_entry = tk.Entry(master)
        self.query_entry.pack()

        self.answer_button = tk.Button(master, text="Get Answer", command=self.get_answer)
        self.answer_button.pack()

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        amount = float(self.amount_entry.get())
        self.expense_tracker.add_expense(date, category, description , amount)
        messagebox.showinfo("Success", "Expense added successfully!")

    def view_expenses(self):
        expenses = self.expense_tracker.view_expenses()
        messagebox.showinfo("Expenses", str(expenses))

    def set_budget(self):
        budget = float(self.amount_entry.get())
        self.budget_manager.set_budget(budget)
        messagebox.showinfo("Success", "Budget set successfully!")

    def check_budget(self):
        amount = float(self.amount_entry.get())
        if self.budget_manager.check_budget(amount):
            messagebox.showinfo("Success", "You are within budget!")
        else:
            messagebox.showerror("Error", "You are over budget!")

    def add_goal(self):
        goal = self.description_entry.get()
        self.financial_goal.add_goal(goal)
        messagebox.showinfo("Success", "Goal added successfully!")

    def view_goals(self):
        goals = self.financial_goal.view_goals()
        messagebox.showinfo("Goals", str(goals))

    def get_answer(self):
        query = self.query_entry.get()
        answer = self.ai_assistant.answer_query(query)
        messagebox.showinfo("Answer", str(answer))

root = tk.Tk()
gui = GUI(root)
root.mainloop()