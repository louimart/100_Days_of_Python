# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# greet_with_name("Jack Bauer")

# functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# greet_with("Louis", "Maple Grove")
greet_with(location = "Maple Grove", name = "Louis")