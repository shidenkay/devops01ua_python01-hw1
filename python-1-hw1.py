#!/usr/bin/env python3
import operator

#Map numbers to functions
operations_map = {
    1: operator.add,
    2: operator.sub,
    3: operator.mul,
    4: operator.truediv
    }

#Map numbers to operation names
operations_names_map = {
    1: "addition",
    2: "subtraction",
    3: "multiplication",
    4: "division"
    }

#Define function to handle user input of nubmers
def get_user_input_numbers(sequence_number):
    while True: 
        try:
            user_input = input(f'Please enter the {sequence_number} number: ')   
            user_input = user_input.replace(',', '.')
            return float(user_input)
        except ValueError: 
            print("Invalid input, please enter a number!")

#Define function to handle user input of operations
def get_user_input_operation():
    while True:
        try: 
            user_input = int(input("\nPlease \033[91mselect\033[0m an operation:\n" 
                                   " 1. Addition\n"
                                   " 2. Subtraction\n"
                                   " 3. Multiplication\n"
                                   " 4. Division\n "
                                   "Enter your choice (1-4): "))
            if user_input in range(1,5):
                return user_input
            else:
                print("Invalid choice, please enter a valid operation!")
        except ValueError:
            print("Invalid input, please enter a number!")

#Define the calculation function
def calculator():
    first_num      = get_user_input_numbers("first")
    second_num     = get_user_input_numbers("second")
    user_choice    = get_user_input_operation()
    operation      = operations_map[user_choice]
    operation_name = operations_names_map[user_choice]

    try:
        result = operation(first_num, second_num)
        print(f'\nThe result of {operation_name} is: {result}')
    except ZeroDivisionError:
        print("Cannot divide by zero!")

#Define function to continue calculating
def continue_calculating():
    while True:
        calculator()
        while True:
            continue_calculating = input("\nWould you like to perform another operation? Enter 'yes' or 'no': ")
            if continue_calculating.lower() in ['yes', 'no']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if continue_calculating.lower() == 'no':
            print("Thank you for using the calculator. Goodbye!")
            break


#Call the main function
print("Welcome to the Calculator Program!\n")
continue_calculating()