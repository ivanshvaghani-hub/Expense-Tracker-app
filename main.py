from function.function import register_user,login_user,add_transaction,update_amount,update_category,update_description,update_income,delete_transaction
import datetime
from database.mysql import get_connection,create_tables

from analytics.analytics import show_data,summary,income_expense_chart,expense_category_chart,category_analysis

def main():
    create_tables()
    
    while(True):
        # print("Welcome Expense Tracker & Analytics")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
        choice = input("Entre you choice:")
        if(choice == "1"):
            username = input("Entre your username:")
            password = input("Create Paaword:")
            register_user(username, password)
            print("Register successful")
            
            
        elif(choice == "2"):
            username = input("Entre your username:")
            password = input("Enter you password:")
            user_id = login_user(username,password)
            if user_id:
                print(f"Login successful! User ID: {user_id}")
                while(True):
                    print("======================================")
                    print("             EXPENSE TRACKER          ")
                    print("======================================")
                    print("1. Add Transaction")
                    print("2. View Transactions")
                    print("3. Update Transaction")
                    print("4. Delete Transaction")
                    print("5. analytics")
                    print("6. Logout")
                    
                    ch = input("Enter your choice:")
                    if(ch == "1"):
                        amount = float(input("Enter amount:"))
                        category = input("Enter category:")
                        transaction_type = input("Enter your type expense or income:")
                        source = input("Enter payment method:")
                        description = input("Enter description:")
                        date = datetime.date.today().isoformat()
                        add_transaction(user_id,amount,category,transaction_type,source,description,date)   
                    elif (ch == "2"):
                           
                        show_data(user_id)
                    elif(ch == "3"):
                        print("What you want yo update")
                        print("1.Amount")
                        print("2.category")
                        print("3.description")
                        print("4.Income")
                        co = input("Enter your choice")
                        if(co == "1"):
                            
                            new_amount = float(input("Enter your new amount:"))
                            update_amount(new_amount,user_id)                
                        elif(co == "2"):
                            new_category = input("Enter your new category:")
                            update_category(new_category,user_id)                
                        elif(co == "3"):
                            new_description = input("Enter your new description:") 
                            update_description(new_description,user_id)
                        elif(co == "4"):
                            new_income = float(input("Add new income:"))
                            update_income(new_income,user_id)
                        else:
                            break               
                    elif(ch == "4"):
                        id = input("Entrer id for delete transaction:")
                        delete_transaction(id)
                    if(ch == "5"):
                        while(True):
                            print("\n========== ANALYTICS ==========")
                            print("1. Financial Summary")
                            print("2. Expense by Category")
                            print("3. Expense Category Chart")
                            print("4. Income vs Expense Chart")
                            print("5. Back") 
                            value = input("Enter your choice:")
                            if (value == "1"):
                                summary(user_id)
                            elif(value=="2"):
                                category_analysis(user_id)
                            elif(value=="3"):
                                expense_category_chart(user_id)
                            elif(value=="4"):
                                income_expense_chart(user_id)
                            else:
                                break
                    if(ch == "6"):
                        break    
        else:
            print("Thank you for visiting")
            break
            
if __name__ == "__main__":
    main()