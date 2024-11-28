def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is you first name?"), input("What is your last name?")))

# Challenge to create a function that checks if a given input year is a leap year
def is_leap_year(year):
    # check if year is divisible by 4
    if year % 4 == 0:
        # check if year is not divisible by 100
        if year % 100 != 0:
            return True
        # if year is divisible by 100 and also divisible by 400
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False


print(f"is leap year {is_leap_year(2100)}")
print(2100 % 4)
print(2100 % 100)
print(2100 % 400)
