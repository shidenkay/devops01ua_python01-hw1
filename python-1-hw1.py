#!/usr/bin/env python3


#Define function to accept user input 

def get_user_input(sequence_number):
    user_input = int(input(f'Please enter {sequence_number} number: ')) 
    return user_input

#For debug
print(get_user_input("first"))
print(get_user_input("second"))
