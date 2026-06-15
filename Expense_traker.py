print("welcome to Expense Tracker ")

exit=True
total=0
expenses=[]
while (exit):

    print("======= Menu =======")
    print("1. Add Expense \n2. View All Expense \n3.View Total Spending \n4. Exit")
    user_choice=input("Enter your choice (1-4): ")
    if(user_choice=='1'):
        date=input("Enter the date of expense (DD-MM-YYYY): ")
        amount=int(input("Enter the amount: "))
        category=input("write category of your expense: ")
        description=input("write discription of expense (if any): ")
        print()
        expense={
            "Date":date,
            "Amount":amount,
            "Category":category,
            "Description":description
        }
        expenses.append(expense)
        
    elif(user_choice=='2'):
        i=1
        print()
        for el in expenses:
            print(f"Data of your {i} expense")
            print(f"Date : {el['Date']}, Amount : {el['Amount']}, Category : {el['Category']}, Description : {el['Description']}")
            print()
            i+=1
    elif(user_choice=='3'):
        print()
        
        for el in expenses:
            total+=el["Amount"]
           
        print("Total spending :",total)    
        print()
    elif(user_choice=='4'):
        print("Thanks you !!")
        break        
    else:
        print("Invalid choice")
        print()