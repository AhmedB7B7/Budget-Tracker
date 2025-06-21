class Transaction:
    def __init__(self, amount, category, description, is_income):
        self.amount = amount
        self.category = category
        self.description = description
        self.is_income = is_income
class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.is_income)
        expense = sum(t.amount for t in self.transactions if not t.is_income)
        return income - expense

    def show_summary(self):
        print("\n=== Budget Summary ===")
        print(f"Total Balance: ${self.get_balance():.2f}")
        for t in self.transactions:
            sign = "+" if t.is_income else "-"
            print(f"{sign}${t.amount:.2f} | {t.category} | {t.description}")

def main():
    tracker = BudgetTracker()

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1" or choice == "2":
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Rent): ")
            description = input("Enter description: ")
            is_income = choice == "1"
            t = Transaction(amount, category, description, is_income)
            tracker.add_transaction(t)
        elif choice == "3":
            tracker.show_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

