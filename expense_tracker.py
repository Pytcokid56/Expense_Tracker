expenses = []
while True: 
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. View Total")
  print("4. Quit")
  
  choice = input("Pick either 1, 2, 3, or 4: ")
  
  if choice == "1":
    print("Enter expense")
    try:
      amount = float(input("Amount: $ "))
    except ValueError:
      print("Try a dollar amount. ex: 12.50")
      continue
    category = input("Category: ")
    description = input("Description: ")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    print("Expense Added!")
  elif choice == "2":
    if len(expenses) == 0:
      print("No Expenses Yet")
    else:
      for expense in expenses:
        print(f"Category: {expense['category']} - Amount: ${expense['amount']:.2f} - Description: {expense['description']}")
  elif choice == "3":
    total = 0
    for expense in expenses:
      total = total + expense['amount']
    print(f"Total ${total:.2f}")
  elif choice == "4":
    print("GoodBye")
    break
  else:
    print("Invalid Choice. Please Pick 1, 2, 3, or 4.")
    
