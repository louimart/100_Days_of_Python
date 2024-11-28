# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
new_bids = "y"
bids = {}

while new_bids.lower() == "y":
    name = input("What is your name?\n")
    price = int(input("What is your bet price?\n$"))
    bids[name] = price
    new_bids = input("Enter more bids? Y or N\n")
    print("\n" * 20)

print(bids)

highest_bidder = ""
bid_amount = 0

for bid in bids:
    if bids[bid] > bid_amount:
        bid_amount = bids[bid]
        highest_bidder = bid
print(f"The highest bidder goes to: {highest_bidder}")