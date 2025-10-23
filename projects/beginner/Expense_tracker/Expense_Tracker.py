import csv
import os
import matplotlib.pyplot as plt

FILENAME = "expenses.csv"

# Ensure file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Category", "Description"])

# Add transaction
def add_transaction():
    t_type = input("Enter type (income/expense): ").strip().lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Rent, Salary): ").capitalize()
    desc = input("Enter short description: ")

    with open(FILENAME, "a", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([t_type, amount, category, desc])

    print("Transaction added successfully!\n")

# Show summary
def show_summary():
    income = 0
    expense = 0
    category_expenses = {}

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Type"] == "income":
                income += float(row["Amount"])
            elif row["Type"] == "expense":
                expense += float(row["Amount"])
                category = row["Category"]
                category_expenses[category] = category_expenses.get(category, 0) + float(row["Amount"])

    balance = income - expense

    print("\n---  Summary ---")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Current Balance: ₹{balance}\n")

    if category_expenses:
        #  Pie chart
        plt.pie(category_expenses.values(), labels=category_expenses.keys(), autopct='%1.1f%%')
        plt.title("Expense Breakdown by Category")
        plt.show()
    else:
        print("No expenses recorded yet.")

# Main Menu
def main():
    while True:
        print("========= Expense Tracker =========")
        print("1. Add Transaction")
        print("2. Show Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
