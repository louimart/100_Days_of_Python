# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# Import and print the logo
import art
print(art.logo)

# defining variable for use in while loops which checks if new bids are needed.
new_bids = "y"
# creating a dictionary for bids
bids = {}

# using while loop, the program keeps repeating asking for bids as long as "Y" is true.
while new_bids.lower() == "y":
    # taking in inputs and assigning to variables
    name = input("What is your name?\n")
    price = int(input("What is your bet price?\n$"))
    # adding the inputs as key and value in the bids dictionary.
    bids[name] = price
    # asking if new bids are needed to continue program or terminate.
    new_bids = input("Enter more bids? Y or N\n")
    # if "y", blank lines create a break in the code to hide previous bid from view.
    print("\n" * 20)

print(bids)

# variables to be used in the for loop below.
highest_bidder = ""
bid_amount = 0

# for every bid in the list of bids, it checks if the bid is higher than bid_amount.
# if higher than bid_amount, highest bidder and bid_amount is updated accordingly.
for bid in bids:
    if bids[bid] > bid_amount:
        bid_amount = bids[bid]
        highest_bidder = bid
print(f"The highest bidder goes to: {highest_bidder}")