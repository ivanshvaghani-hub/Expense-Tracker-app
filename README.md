# 💰 Expense Tracker & Analytics

A Python-based **Expense Tracker & Analytics** application that allows users to register, log in, manage their income and expenses, and analyze their financial transactions.

The project uses **Python, SQLite, Pandas, and Matplotlib** to provide a simple command-line expense management and data analytics system.

---

## 📌 Project Overview

Managing daily expenses manually can make it difficult to understand where money is being spent.

This project provides a simple system where users can:

- Create an account
- Log in securely
- Add income and expense transactions
- Store transaction details in an SQLite database
- View their transactions
- Update transactions
- Delete transactions
- Track transaction categories
- Store payment methods
- Store income sources
- Automatically record transaction dates
- Analyze transaction data using Pandas
- Generate financial charts using Matplotlib

The main purpose of this project is to combine **Python programming, database management, and data analysis** into one practical application.

---

# ✨ Features

## 👤 User Management

### 1. Register

New users can create an account using:

- Username
- Password

User information is stored in the SQLite database.

### 2. Login

Registered users can log in using:

- Username
- Password

The application checks the entered credentials against the database.

### 3. Logout

Users can safely return to the main menu after completing their transactions.

---

# 💳 Transaction Management

After successful login, users can manage their financial transactions.

The transaction menu contains:

```text
1. Add Transaction
2. View Transactions
3. Update Transaction
4. Delete Transaction
5. Logout

➕ Add Transaction

Users can add a new transaction by entering information such as:

User ID
Amount
Category
Transaction Type
Payment Method / Source
Description
Date

📋 View Transactions

Users can view transactions belonging to their user ID.

The application retrieves transaction data from SQLite and can convert it into a Pandas DataFrame.

✏️ Update Transaction

Users can modify an existing transaction.

For example, they can update:

Amount
Category
Transaction type
Source
Description
Date

This allows users to correct incorrect transaction information.

🗑️ Delete Transaction

Users can delete transactions that are no longer required.

The transaction is removed from the SQLite database.

📊 Data Analytics

The project uses Pandas and Matplotlib for analyzing financial data.

Pandas is used to:

Load transaction data
Create DataFrames
Filter data
Group transactions
Calculate totals
Analyze categories
Analyze income and expenses

Matplotlib is used to create visualizations.

Possible analytics include:

Total income
Total expenses
Balance
Expenses by category
Income by source
Monthly expenses
Transaction distribution

🏗️ Project Structure

The project is organized into different modules.

Expense Tracker & Analytics/
│
├── database/
│   ├── mysql.py
│   └── __pycache__/
│
├── function/
│   ├── function.py
│   └── __pycache__/
│
├── analytics/
│   └── analytics.py
│
├── expenses.db
│
├── main.py
│
└── README.md
