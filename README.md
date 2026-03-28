💰 Personal Expense Tracker

A simple command-line application to track your daily expenses, built with Python.

📌 Problem Statement

Managing personal finances is a common challenge, especially for students. Most budgeting apps are complex or cloud-based. This tool solves that with a lightweight, local, terminal-based tracker that requires no internet connection or account.

✨ Features

Add expenses with date, category, amount, and description
View all recorded expenses in a formatted table
Filter expenses by category
View a spending summary with percentage breakdown
Data saved locally in a CSV file — persists between sessions

🛠️ Requirements

Python 3.6 or higher

No external libraries needed — uses only the Python standard library

🚀 Setup & Usage

1. Clone the Repository
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```
2. Run the App
```bash
python expense_tracker.py
```
3. Using the Menu
```
========================================
   💰 Personal Expense Tracker
========================================

Menu:
  1. Add Expense
  2. View All Expenses
  3. Filter by Category
  4. View Summary
  5. Exit
```
Add Expense — Enter date (or press Enter for today), pick a category, enter amount and an optional description
View All Expenses — See every recorded expense with a running total
Filter by Category — View expenses under a specific category (Food, Transport, etc.)
View Summary — See total spending per category with percentage breakdown
📁 Project Structure
```
expense-tracker/
│
├── expense_tracker.py   # Main application file
├── expenses.csv         # Auto-created when first expense is added
└── README.md            # This file
```
💡 Example Output
```
Date         Category          Amount   Description
------------------------------------------------------------
2025-03-20   Food             ₹150.00   Lunch at canteen
2025-03-21   Transport         ₹50.00   Auto fare
2025-03-22   Bills            ₹499.00   Mobile recharge
------------------------------------------------------------
TOTAL                         ₹699.00
```
🔮 Future Improvements
Monthly budget limits with alerts
Export summary as a `.txt` report
Filter by date range
Graphical charts using `matplotlib`

---
Built as part of a Python Programming course (BYOP project)
