# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# common formatting of dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])

# how to add into the dictionary.
# set the dictionary[key] = value
programming_dictionary["Loop"] = "action of doing something over and over again"
print(programming_dictionary["Loop"])

# how to clear a dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit and item in a dictionary
# will look for key in dictionary, if no match will add a new entry.
programming_dictionary["Bug"] = "a moth in your computer"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])