import random

#create a list with 52 cards
card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
card_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card_list = []
card_list_21 = []

#creating the 52 cards
for i in card_numbers:
    for o in card_suit:
        card_list.append(i + " of " + o)

#randomly select 21 card from the list of 52 cards
while len(card_list_21) < 21:
    cards = random.choice(card_list)
    if cards == cards:
        card_list_21.append(cards)

#lay out the 21 cards in 3 stacks of 7, row by row, not column by column
print(card_list_21)

#get the player to tell you what pile their card is in. 1, 2 or 3.
#place the pile of selected cards in the middle of the other two piles.
#lay out the 21 cards in 3 stacks of 7, row by row, not column by column
#get the player to tell you which pile the card is in now. 1, 2, or 3.
#place the pile of selected cards in the middle of the other two piles.
#lay out the 21 cards in 3 stacks of 7, row by row, not column by column
#get the player to tell you which pile the card is in now. 1, 2, or 3.
#grab the pile according to the answer given
#if the trick is performed correctly, the chosen card will always be eleventh
#References
