from datetime import date
from datetime import datetime
import json


    
expense_store = []

def add_expense():
    dict = {
        "category": category,
        "amount": amount,
        "note": note,
        "date": today,
        "time": time
    }
    expense_store.append(dict)
    return expense_store

def view_expense():
     for items in expense_store:
          print(f"{items['category']} | {items['amount']} | {items['note']} | {items['date']} {items['time']}")

while True:
    category = input('What type of product is it: ')
    if category == "stop":
         break
    try:
        amount = int(input('Amount:'))
        if amount < 1:
            print("enter a value above 0")
            continue
    except ValueError:
        print("enter a valid number")
        continue
    note = input('Note: ')

    today = date.today().strftime("%d-%m-%Y")
    time = datetime.now().strftime("%H:%M:%S")

    add_expense()


def filter_by_category():
    sort_by = input("sort category by: ").lower()
    found = False
    for items in expense_store:
        if(items['category'].lower() == sort_by):
            print(f"{items['category']} | {items['amount']} | {items['note']} | {items['date']} {items['time']}")
            found = True
    if not found:
        print("not found")  

def total_by_category():
    sort_by = input("sort category by: ").lower()
    total = 0
    found = False
    for items in expense_store:
        if(items["category"].lower() == sort_by):
            total += items["amount"]
            found = True
    if not found:
        print("this catrgory was not found")
    else:
        print(f"the total of the {sort_by} category: {total}")

def total_spending():
    total = 0
    for items in expense_store:
        total += items["amount"]
    print(f"this is the total of all the expenditure: {total}")

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expense_store = json.load(file)
        print("expense loaded")
    except FileNotFoundError:
        print("no saved expense file found")
        expense_store = []
    except json.JSONDecodeError:
        print("file is corrupted or not valid json")
        expense_store = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expense_store, file, indent=4)
    print("Expenses saved successfully.")

while True:
    print("1. View all\n2. Filter by category\n3. Total spending\n4. Total by category\n5. Save expenses\n6. Load expenses\n7. Exit")

    menu_input = int(input("Choose your function number: ")) 

    try:
        if menu_input == 1:
            view_expense()
        elif menu_input == 2:
            filter_by_category()
        elif menu_input == 3:
            total_spending()
        elif menu_input == 4:
            total_by_category()
        elif menu_input == 5:
            save_expenses()
        elif menu_input == 6:
            load_expenses()
        #elif menu_input == 8:
            #add_expense()
        elif menu_input == 7: 
            break
        else: 
            print("invalid command")
            continue
    except ValueError:
        print("the input has to be a number")
   


