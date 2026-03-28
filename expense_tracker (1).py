import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]


def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    """Add a new expense entry."""
    print("\n--- Add Expense ---")

    # Date input
    date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_input = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today's date.")
            date_input = datetime.today().strftime("%Y-%m-%d")

    # Category input
    print("Categories:", ", ".join(f"{i+1}. {c}" for i, c in enumerate(CATEGORIES)))
    cat_choice = input("Choose category (1-6): ").strip()
    try:
        category = CATEGORIES[int(cat_choice) - 1]
    except (ValueError, IndexError):
        category = "Other"

    # Amount input
    while True:
        try:
            amount = float(input("Amount (₹): ").strip())
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number.")

    # Description
    description = input("Description (optional): ").strip() or "No description"

    # Save to CSV
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date_input, category, f"{amount:.2f}", description])

    print(f"\n✅ Expense of ₹{amount:.2f} added under '{category}'.")


def view_expenses():
    """Display all expenses in a formatted table."""
    print("\n--- All Expenses ---")
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"\n{'Date':<12} {'Category':<15} {'Amount':>10}  {'Description'}")
    print("-" * 60)
    total = 0
    for row in expenses:
        print(f"{row['Date']:<12} {row['Category']:<15} ₹{float(row['Amount']):>8.2f}  {row['Description']}")
        total += float(row["Amount"])
    print("-" * 60)
    print(f"{'TOTAL':<28} ₹{total:>8.2f}")


def filter_expenses():
    """Filter expenses by category."""
    print("\n--- Filter by Category ---")
    print("Categories:", ", ".join(f"{i+1}. {c}" for i, c in enumerate(CATEGORIES)))
    cat_choice = input("Choose category (1-6): ").strip()

    try:
        category = CATEGORIES[int(cat_choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    expenses = load_expenses()
    filtered = [e for e in expenses if e["Category"] == category]

    if not filtered:
        print(f"No expenses found for '{category}'.")
        return

    print(f"\n--- Expenses: {category} ---")
    print(f"\n{'Date':<12} {'Amount':>10}  {'Description'}")
    print("-" * 45)
    total = 0
    for row in filtered:
        print(f"{row['Date']:<12} ₹{float(row['Amount']):>8.2f}  {row['Description']}")
        total += float(row["Amount"])
    print("-" * 45)
    print(f"{'TOTAL':<13} ₹{total:>8.2f}")


def summary():
    """Show spending summary by category."""
    print("\n--- Spending Summary ---")
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    grand_total = 0
    for row in expenses:
        cat = row["Category"]
        amt = float(row["Amount"])
        totals[cat] = totals.get(cat, 0) + amt
        grand_total += amt

    print(f"\n{'Category':<20} {'Total':>10}  {'% of Spend'}")
    print("-" * 45)
    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        pct = (amt / grand_total) * 100
        print(f"{cat:<20} ₹{amt:>8.2f}  {pct:.1f}%")
    print("-" * 45)
    print(f"{'GRAND TOTAL':<20} ₹{grand_total:>8.2f}")


def load_expenses():
    """Load all expenses from the CSV file."""
    expenses = []
    with open(FILE_NAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(row)
    return expenses


def main():
    initialize_file()
    print("=" * 40)
    print("   💰 Personal Expense Tracker")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("  1. Add Expense")
        print("  2. View All Expenses")
        print("  3. Filter by Category")
        print("  4. View Summary")
        print("  5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            summary()
        elif choice == "5":
            print("\nGoodbye! Keep tracking your expenses. 👋")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
