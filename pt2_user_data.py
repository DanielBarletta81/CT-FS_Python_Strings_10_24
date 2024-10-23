

#Task 1: Input Length Validator 
# 
# Write a script that asks for and checks the length 
# of the user's first name and last name. Both should be at least 2 characters long.
#  If not, print an error message.

#NOTE: Ensure that all code in your file is ready to run. 
# This means that if someone opens your file and clicks the run button at the top,
#  all code executes as intended. For example, if there are if statements, 
# print statements, or for loops, they should function correctly and display 
# output in the console as expected. 
# 
# If you have a function, make sure the function is called and runs.




#

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")

if len(user_first_name) <= 2:
    print(f"Error! You entered {user_first_name}. First name must be more than 2 characters.")
elif len(user_last_name) <= 2:
    print(f"Error! You entered {user_last_name}. Last name must be more than 2 characters.")
else:
    print(f"Welcome {user_first_name} {user_last_name}")