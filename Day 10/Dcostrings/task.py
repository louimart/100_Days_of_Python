def format_name(f_name, l_name):
    """Takes a first name and last name and returns a formated full name in Title Case"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



