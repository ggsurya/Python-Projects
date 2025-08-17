# 💰 Expense Tracker in Python

A simple command-line Python program to track personal expenses.

## Features

- Add new expenses with date, category, description, and amount.
- View all recorded expenses in a neat tabular format.
- Delete specific expenses by date and description.
- Automatically stores data in a CSV file (expenses.csv).
- Handles invalid inputs gracefully.

## Usage

1. Clone the repository or download the source code file.
2. Run the program with Python 3. For example:
   ```bash
   python expense_tracker.py
3. Use the menu to add, view, or delete expenses.

## Example

```
Expense Tracker
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit
Enter your choice: 1

Enter date (YYYY-MM-DD): 2025-08-17
Enter category (e.g., Food, Transport): Food
Enter description: Lunch
Enter amount: 12.50
Expense added successfully!

Expense Tracker
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit
Enter your choice: 2

======================================================================
Date         | Category        | Description               |     Amount
----------------------------------------------------------------------
2025-08-17   | Food            | Lunch                     |      12.50
======================================================================
Total expenses: 1
```

## How the Program Works

- Expenses are stored in a CSV file (expenses.csv).
- Each expense has a date, category, description, and amount.
- You can view all expenses in a formatted table.
- Specific expenses can be deleted by providing the date and description.
- Input validation ensures numeric amounts and handles empty records.
   
## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ggsurya/Python-Projects/blob/main/LICENSE) file for details.

## 📩 Contact

**G.G. Surya**  
📧 Email: ggsuryaff@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/g-g-surya-5aa9312b4)
🔗 [GitHub](https://github.com/ggsurya)
