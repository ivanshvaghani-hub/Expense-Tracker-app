import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def get_data(user_id):

    con = sqlite3.connect("expenses.db")

    query = """
    SELECT *
    FROM transactions
    WHERE user_id = ?
    """

    df = pd.read_sql_query(query, con, params=(user_id,))

    con.close()

    return df


def show_data(user_id):

    df = get_data(user_id)

    if df.empty:
        print("No transactions found.")
        return

    print("\n========== TRANSACTIONS ==========")
    print(df)
    
    
def summary(user_id):
    
    df = get_data(user_id)
    
    if df.empty:
            print("No transactions found.")
            return
    
    income = df[df["type"] == "income"]["amount"].sum()
    expense = df[df["type"] == "expense"]["amount"].sum()
    
    balance = income - expense
    
    print("====================================")
    print("              SUMMARY               ")
    print("====================================")
    
    print("Income:",income)
    print("expense:",expense)
    print("balance:",balance)
    
def category_analysis(user_id):

    df = get_data(user_id)

    expense_df = df[df["type"] == "expense"]

    if expense_df.empty:
        print("No expense data found.")
        return

    category_total = expense_df.groupby("category")["amount"].sum()

    print("\n========== EXPENSE BY CATEGORY ==========")
    print(category_total)
    
def expense_category_chart(user_id):

    df = get_data(user_id)

    expense_df = df[df["type"] == "expense"]

    if expense_df.empty:
        print("No expense data found.")
        return

    category_total = expense_df.groupby("category")["amount"].sum()

    category_total.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Expense by Category")
    plt.ylabel("")
    plt.show()
    
def income_expense_chart(user_id):

    df = get_data(user_id)

    if df.empty:
        print("No transaction data found.")
        return

    total = df.groupby("type")["amount"].sum()

    total.plot(kind="bar")

    plt.title("Income vs Expense")
    plt.xlabel("Transaction Type")
    plt.ylabel("Amount")

    plt.show()

    