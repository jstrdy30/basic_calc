#Python project | Simple CalcuLATER

import time

#Operations
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
choice = int(input("\nEnter your choice: "))

#Choosing a number
if choice in (1,2,3,4):
    choice_1 = float(input("\nEnter your first number: "))
    choice_2 = float(input("Enter your second number: "))
    
    if choice == 1:
        print(f"\n{choice_1} + {choice_2} = {choice_1 + choice_2}")
    elif choice == 2:
        print(f"\n{choice_1} - {choice_2} = {choice_1 - choice_2}")
    elif choice == 3:
        print(f"\n{choice_1} × {choice_2} = {choice_1 * choice_2}")
    elif choice == 4:
        print(f"\n{choice_1} ÷ {choice_2} = {choice_1 / choice_2}")

elif choice == 5:
     quit()
    
      
    
        
        
else:
    print("Invalid Input!!!")