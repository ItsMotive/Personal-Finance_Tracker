## Part 2: Designing the Application
## Step 1: Define Application Requirements
    • Core Features:
        1. Income Tracker: Allows users to log their sources of income, including salary, freelance work, etc.
        2. Expense Tracker: Enables users to categorize and log their expenses (e.g., rent, groceries, entertainment).
        3. Savings Goals: Users can set and track savings goals, such as saving for a vacation or emergency fund.
        4. Reporting: Provides visual reports of income vs. expenses, category-wise expense breakdown, and progress toward savings goals.

    • Optional Features:
        1. Budgeting: Allows users to set monthly budgets for different categories and alerts them when they exceed the budget.
        2. Recurring Transactions: Automatically logs recurring transactions like rent or subscriptions.

## Step 2: Design the Database Schema
    • Tables:
        1. Income Table: id, source, amount, date
        2. Expense Table: id, category, amount, date, description
        3. Savings Table: id, goal, target_amount, current_amount, target_date

    • Database Setup:
        1. Create the SQLite database and define the schema using Python.
        2. Write functions to insert, update, and delete records from each table.