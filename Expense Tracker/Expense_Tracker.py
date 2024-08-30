expenses = []

def add_expense(description, amount):
    expense = {
        'description': description,
        'amount': amount
    }
    expenses.append(expense)


def view_expense():
    if  not expenses:
        print("no Expenses Record")
        return
    if expenses:
        for expense in expenses:
            print(f"Description {expense['description']} Amount ${expense['amount']:.2f}")

def total_expenses():
    total = sum(expense ['amount'] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Exit")


        choice = input("Enter your method number: ")

        if choice ==  "1":
            n_expenses = int(input("How many expenses you want to add? "))
            for i in range(n_expenses):
                description = input("Enter expense description: ")
                amount = float(input("Enter amount: "))
                add_expense(description, amount)

        if choice == "2":
            print("Your Expense: ")
            view_expense()
        
        if choice == "3":
            print("your total expenses: ")
            total_expenses()
        
        if choice == "4":
            print("Have a nice day")
            break
if __name__ == "__main__":
    main()

