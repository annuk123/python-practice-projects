#import the random module... where module is a file containing python code(.py) that can include function, classes, variables or any runnable statements
#3 types of module: 1. built-in  2. user-defined modules 3. external modules
# a package is a folder or directry containing multiple modules and special __init__.py file.
# library, it is the collection of related packages and module bundled together...


#project idea:  i have to build a cmd line untility that generates strong, randomized password based on user defined lengths and criteria...

# before building this, decide what makes my password generator smart and secure.
# then think through how passwords should be generated, how their length is selected and how character types are handled
# then think which concept is going to apply in your project... like here we will apply strings, loops, conditional fuctions, modules, exception handeling
# then understand about security, like randomness, password entropy, character-set size, and why ordinary pseudorandom generators aren't suitable for security-sensitive passwords...
# and the last but not the least, consider edge cases, invalid inputs, and how we can verify that my generator behaves correctly...
# pick and inquirer library

import secrets
from string import ascii_letters, punctuation, digits, ascii_lowercase, ascii_uppercase
password_length = 12
min_password_length = 8
max_password_length =  50
lowercase = ascii_lowercase
while True:
    password_length_choice = input("do you want 12 length long character in your password(yes/no): ").strip().lower()
    if password_length_choice in ["yes", 'y']:
        print("your password length is 12")
        break
    elif password_length_choice in ["no", 'n']:
        try:
            new_password_length = int(input("Enter your desire length password: "))
            if min_password_length <=  new_password_length <= max_password_length:
                password_length = new_password_length
                print(f"Your password length is {password_length}")
                break
            else:
                print(f"put your password between {min_password_length} to {max_password_length} ")
        except ValueError:
            print("Enter the correct password length: ")
    else:
        print("Your password length is invalid...")




while True:
    lowercase_letter = input("Do you want lowercase letter(y/n): ").strip().lower()
    if lowercase_letter in ["yes", "y"]:
        include_lowercase = bool(lowercase_letter) 
        print(f"in your password lowercase added as {include_lowercase}")
        break
    elif lowercase_letter in ["no", "n"]:
        include_lowercase = bool(lowercase_letter) 
        print(f"okay we will set you password {include_lowercase} lowercase")
        break
    else:
        print("add valid letter")




        


   

