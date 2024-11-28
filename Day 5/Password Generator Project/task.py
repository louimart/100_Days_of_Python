import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# letter_length = len(letters)
# number_length = len(numbers)
# symbol_length = len(symbols)

# Method 1: concatenated string password
# pw = ""
#
# print(f"randomly selected letter: {random.choice(letters)}")
# print(f"randomly selected number: {random.choice(numbers)}")
# print(f"randomly selected symbol: {random.choice(symbols)}")
#
# for l in range(0, nr_letters):
#     pw += random.choice(letters)
# for l in range(0, nr_symbols):
#     pw += random.choice(symbols)
# for l in range(0, nr_numbers):
#     pw += random.choice(numbers)
#
# print(f"Your Password is: {pw}")

# Method 2: randomized string password
pw = []

for l in range(0, nr_letters):
    # print(f"checking range {l}")
    pw.append(random.choice(letters))
for l in range(0, nr_symbols):
    pw.append(random.choice(symbols))
for l in range(0, nr_numbers):
    pw.append(random.choice(numbers))

print(f"Password before randomization: {pw}")
random.shuffle(pw)
print(f"Randomized Password: {pw}")

random_pw = ""
for char in pw:
    random_pw += char

print(f"Your Randomized Password is: {random_pw}")

# for char in range(0, len(pw)):
#     selected = random.choice(pw)
#     random_pw += selected
#     pw.remove(selected)
