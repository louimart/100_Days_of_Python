# BlackJack Game Project
import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []


# Functions
def deal_hand():
    print(art.logo)
    card_count = 0
    while card_count < 2:
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))
        card_count += 1

def player_hand():
    print(f"Your cards: {player}, current score: {sum(player)}")

def player_final():
    print(f"Your final hand: {player}, final score: {sum(player)}")

def dealer_hand():
    print(f"Dealer's first card: {dealer[0]}")

def dealer_final():
    print(f"Your final hand: {dealer}, final score: {sum(dealer)}")

# Code
deal_input = input("Do you want to play a game of BlackJack? Y or N\n")
if deal_input.lower() == "y":
    deal_hand()
    player_hand()
    dealer_hand()
    while sum(player) <= 21:
        if sum(player) == 21:
            print("you WIN")
            break
        else:
            hit = input("Type 'Y' to get another card, Type 'N' to pass\n")
            if hit.lower() == "y":
                player.append(random.choice(cards))
                player_hand()
                dealer_hand()
            else:
                break
    else:
        player_final()
        dealer_final()

        print("you went over")



elif deal_input.lower() == "n":
    print("come again")




# player_hand()
# print(f"player cards: {player}, total of {player_total}")
