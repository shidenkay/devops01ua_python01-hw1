#!/usr/bin/env python3
import operator

#Define function to accept user input 

def get_user_input(sequence_number):
    while True: 
        try:
            user_input = input(f'Please enter the {sequence_number} number: ')   
            user_input = user_input.replace(',', '.')
            return float(user_input)
        except ValueError: 
            print("ValueError, try again")

def get_user_operation():
    operations = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv
    }
    while True:
        try: 
            user_input = int(input("""Please select an operation: 
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            Enter your choice (1-4): """))
            if user_input in operations.keys():
                return operations[user_input]
            else:
                print("Invalid choice, please enter a valid operation!")
        except ValueError:
            print("Invalid input, please enter a number!")




#For debug
number1 = get_user_input("first")
number2 = get_user_input("second")
choice = get_user_operation()
result = choice(number1, number2)
print(result)