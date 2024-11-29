import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# print(f'''
# {add(2, 2)}
# {subtract(2, 2)}
# {multiply(2, 2)}
# {divide(2, 2)}
# ''')

operation = {"+": add, "-": subtract, "*": multiply, "/": divide}
# print(operation["*"](4, 8))

use_previous_result = False
continue_operation = True

print(art.logo)
while continue_operation:
    if not use_previous_result:
        first_number = float(input("Please enter a first number\n"))
        operator = input("Please enter an operator: '+', '-', '*', or '/'\n")
        second_number = float(input("Please enter a second number\n"))
        result = operation[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        use_result = input("continue with previous result? 'y' or 'n'\n")
        if use_result == 'y':
            use_previous_result = True
            first_number = result
        else:
            use_previous_result = False
            continue_calculation = input("Would you like to continue? 'y' or 'n'\n")
            if continue_calculation == 'y':
                continue
            elif continue_calculation == 'n':
                continue_operation = False
    else:
        operator = input("Please enter an operator: '+', '-', '*', or '/'\n")
        second_number = float(input("Please enter a second number\n"))
        result = operation[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        use_result = input("Continue calculation with previous result? 'y' or 'n'\n")
        if use_result == 'y':
            use_previous_result = True
            first_number = result
        else:
            use_previous_result = False
            continue_calculation = input("Would you like to continue? 'y' or 'n'\n")
            if continue_calculation == 'y':
                continue
            elif continue_calculation == 'n':
                continue_operation = False