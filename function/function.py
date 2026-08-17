import random
import datetime
from database.mysql import get_connection,create_tables

def register_user(username, password):
    con = get_connection()
    cursor = con.cursor()
    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES (?, ?)",
            (username, password)
        )
        con.commit()
        return True
    except:
        return False
    finally:
        con.close()
        
def login_user(username, password):
    con = get_connection()
    cursor = con.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    con.close()

    if user:
        print("Login successful")
        return user[0]
    else:
        print("Invalid username or password")
        return None
    
    
def add_transaction(user_id, amount, category, transaction_type, source, description, date):
    con = get_connection()
    cursor = con.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (user_id, amount, category, type, source, description, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (user_id, amount, category, transaction_type, source, description, date)
    )

    con.commit()
    con.close()

    print("Transaction added successfully")


def view_transaction(user_id):
    con=get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM transactions WHERE user_id=?",(user_id,))
    rows = cursor.fetchall()
    con.close()
    return rows


def update_amount(new_amount,user_id):
    con=get_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE transactions SET amount = ? WHERE user_id=?",(new_amount,user_id))
    con.commit()
    con.close()
    
    print("Transaction update amount successfully")
    
def update_category(new_category,user_id):
    con=get_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE transactions SET category = ? WHERE user_id=?",(new_category,user_id))
    con.commit()
    con.close()
    
    print("Transaction update category successfully")
    
def update_description(new_description,user_id):
    con=get_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE transactions SET description = ? WHERE user_id=?",(new_description,user_id))
    con.commit()
    con.close()
    
    print("Transaction upadte description successfully")
    
def update_income(new_income,user_id):
    con=get_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE transactions SET income = ? WHERE user_id=?",(new_income,user_id))
    con.commit()
    con.close()
    
    print("Transaction upadte income successfully")
    

def delete_transaction(id):
    con=get_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=?",(id,))
    con.commit()
    con.close()
    
    print("Transaction delete successfully")
