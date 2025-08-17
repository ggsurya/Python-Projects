import csv
import os

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, f"{amount:.2f}"])
    
    print("Expense added successfully!\n")

def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("\nNo expenses found.\n")
        return

    headers = rows[0]
    print("\n" + "=" * 70)
    print("{:<12} | {:<15} | {:<25} | {:>10}".format(*headers))
    print("-" * 70)
    
    for row in rows[1:]:
        print("{:<12} | {:<15} | {:<25} | {:>10}".format(row[0], row[1], row[2], row[3]))
    
    print("=" * 70)
    print(f"Total expenses: {len(rows)-1}\n")

def delete_expense():
    view_expenses()
    date_to_delete = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    description_to_delete = input("Enter the description of the expense to delete: ")

    deleted = False
    with open(FILE_NAME, mode='r') as file:
        rows = list(csv.reader(file))

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in rows[1:]:
            if row[0] == date_to_delete and row[2] == description_to_delete:
                deleted = True
                continue
            writer.writerow(row)

    if deleted:
        print("Expense deleted successfully!\n")
    else:
        print("Expense not found.\n")

def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
