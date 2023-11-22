
# Calculator Main Title ASCII Art 
def print_calculator_art():
    calculator_art = """
_______________________________________________________________.          
_____________________________________________________________. .
   _____      _  _____ _        _   _                        | |
  / ____|    | |/ ____| |      | | (_)                       | |
 | |     __ _| | (___ | |_ __ _| |_ _  ___  _ __             | |
 | |    / _` | |\___ \| __/ _` | __| |/ _ \| '_ \            | |
 | |___| (_| | |____) | || (_| | |_| | (_) | | | |           | |
  \_____\__,_|_|_____/ \__\__,_|\__|_|\___/|_| |_|           | |
**************************************************           | |
[+]Version: 1.0                                              | |
[+]Programmer: Kasun Sajith                                  | |
-------------------------------------------------------------. |
---------------------------------------------------------------. 
                                                
"""
    print(calculator_art)


# Display About Text Function
def display_about_info():
    about_info = f"""
============================================
CalStation Calculator - Version 1.0
Developed by: Kasun Sajith
============================================
This calculator is a simple command-line tool
written in Python. It can perform basic arithmetic
operations such as addition, subtraction,
multiplication, and division.

Feel free to use and modify it as needed!

For more information or to report issues, visit:
https://github.com/python-nerd-git/CalStation
__________________________________________________
"""
    print(about_info)



# Calculator EXIT ASCII Art 
def print_exit_art():
    exit_art = """
______________________________
>>> Exiting the CalStation !!!
______________________________+++ Version -1.0
------------------------------------------------

   _____                 _ _                _ 
  / ____|               | | |              | |
 | |  __  ___   ___   __| | |__  _   _  ___| |
 | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ |
 | |__| | (_) | (_) | (_| | |_) | |_| |  __/_|
  \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                                  __/ |       
                                 |___/        
_________________________________________________  
                                                                                    
"""
    print(exit_art)


# defining All the main Maths Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Main function
def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("6. About the Program\n")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '5':
            # Run the function to print the exit art
            print_exit_art()
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("------------------------------------------")
                print(f">>> {num1} + {num2} = {add(num1, num2)}    [+] Answer = {add(num1, num2)}")
                print("------------------------------------------\n")

            elif choice == '2':
                print("------------------------------------------")
                print(f">>> {num1} - {num2} = {subtract(num1, num2)}  [+] Answer = {subtract(num1, num2)}")
                print("------------------------------------------\n")

            elif choice == '3':
                print("------------------------------------------")
                print(f">>> {num1} * {num2} = {multiply(num1, num2)}  [+] Answer = {multiply(num1, num2)}")
                print("------------------------------------------\n")

            elif choice == '4':
                print("------------------------------------------")
                result = divide(num1, num2)
                print(f">>> {num1} / {num2} = {result}  [+] Answer = {result}")
                print("------------------------------------------\n")
                
        elif choice == '6':
            # Optionally, display about info
            display_about_info()  

        else:
            print(f"\n[{choice}]***Invalid input. Please enter a valid option !!!\n")




# Run the function to print the calculator art
print_calculator_art()

# Run the CalStation calculator
calculator()
