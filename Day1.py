import json
import os

DATA_FILE = "data.json"

# -------------------- DATA HANDLING --------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# -------------------- ADD TRANSACTIONS --------------------

def add_transaction(transaction_type):
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Enter category: ").strip()
    month = input("Enter month (e.g. January): ").strip()

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "month": month
    }

    data = load_data()
    data.append(transaction)
    save_data(data)

    print(f"{transaction_type.capitalize()} added successfully!")

# -------------------- MONTHLY REPORT --------------------

def generate_monthly_report():
    month = input("Enter month for report: ").strip()
    data = load_data()

    income = 0
    expense = 0

    for t in data:
        if t["month"].lower() == month.lower():
            if t["type"] == "income":
                income += t["amount"]
            elif t["type"] == "expense":
                expense += t["amount"]

    savings = income - expense

    print("\n MONTHLY REPORT")
    print(f"Month: {month}")
    print(f"Total Income: ₹{income}")
    print(f"Total Expenses: ₹{expense}")
    print(f"Savings: ₹{savings}\n")

# -------------------- MAIN FUNCTION --------------------

def main():
    while True:
        print("\n====== Personal Finance Tracker ======")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Monthly Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expense")
        elif choice == "3":
            generate_monthly_report()
        elif choice == "4":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

# -------------------- PROGRAM START --------------------

if __name__ == "__main__":
    main()