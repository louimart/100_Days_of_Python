# def my_function():
#     return 3 * 2
#
# output = my_function()
# print(output)

# def format_name():
#     f_name = input("What is your first name?\n")
#     l_name = input("What is your last name?\n")
#     print( f_name + " " + l_name)

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # everything after the return replaces where the function is being called.
    return f"{formated_f_name} {formated_l_name}"

print(format_name("LOUIS", "mARTIN"))

def function_1(text):
    return text + " " + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)