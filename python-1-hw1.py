#!/usr/bin/env python3


#Define function to accept user input 

def get_user_input(sequence_number):
    while True: 
        try:
            user_input = input(f'Please enter {sequence_number} number: ')   
            user_input = user_input.replace(',', '.')
            return float(user_input)
        except ValueError: 
            print("ValueError, try again")
#        finally:
#            print("Success!")

#For debug
print(get_user_input("first"))
print(get_user_input("second"))
