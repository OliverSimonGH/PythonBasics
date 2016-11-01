import random, os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    #create a list with 52 cards
    card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_list_52 = []
    card_list_21 = []
    row_one = []
    row_two = []
    row_three = []
    middle_deck = []

    #creating the deck of cards
    for i in card_numbers:
        for o in card_suit:
            card_list_52.append(i + " of " + o)

    #randomly select 21 card from the list of 52 cards
    while len(card_list_21) < 21:
        card = random.choice(card_list_52)
        card_list_21.append(card)
        card_list_52.remove(card)

    #lay out the 21 cards, and puts them in rows, they do not get shuffled yet.
    while len(card_list_21) > 0:
        random_card = random.choice(card_list_21)
        row_one.append(random_card)
        card_list_21.remove(random_card)

        random_card = random.choice(card_list_21)
        row_two.append(random_card)
        card_list_21.remove(random_card)

        random_card = random.choice(card_list_21)
        row_three.append(random_card)
        card_list_21.remove(random_card)
    print("Row one: {} \nRow two: {} \nRow three: {}".format(row_one, row_two, row_three))

    #get the player to tell you what pile their card is in. 1, 2 or 3.
    #place the pile of selected cards in the middle of the other two piles.
    def pick_a_row():
        input_answer = input("What row is your card in (1)(2)(3): ")
        if input_answer == "1":
            for i in range(7):
                middle_deck.append(row_two[i])
            for i in range(7):
                middle_deck.append(row_one[i])
            for i in range(7):
                middle_deck.append(row_three[i])

        elif input_answer == "2":
            for i in range(7):
                middle_deck.append(row_one[i])
            for i in range(7):
                middle_deck.append(row_two[i])
            for i in range(7):
                middle_deck.append(row_three[i])

        elif input_answer == "3":
            for i in range(7):
                middle_deck.append(row_one[i])
            for i in range(7):
                middle_deck.append(row_three[i])
            for i in range(7):
                middle_deck.append(row_two[i])
        else:
            pick_a_row()

    def clear_row():
        row_one.clear()
        row_two.clear()
        row_three.clear()

    def shuffle():
        while len(middle_deck) > 0:
            card = (middle_deck[0])
            row_one.append(card)
            middle_deck.remove(card)

            card = (middle_deck[0])
            row_two.append(card)
            middle_deck.remove(card)

            card = (middle_deck[0])
            row_three.append(card)
            middle_deck.remove(card)
        print("Row one: {} \nRow two: {} \nRow three: {}".format(row_one, row_two, row_three))


    #lay out the 21 cards in 3 stacks of 7, row by row, not column by column
    #get the player to tell you which pile the card is in now. 1, 2, or 3.
    pick_a_row()
    clear_row()
    shuffle()

    #place the pile of selected cards in the middle of the other two piles.
    # #lay out the 21 cards in 3 stacks of 7, row by row, not column by column
    # #get the player to tell you which pile the card is in now. 1, 2, or 3.
    pick_a_row()
    clear_row()
    shuffle()
    #grab the pile according to the answer given
    pick_a_row()
    print("Your answer is: {}".format(middle_deck[10]))
    #if the trick is performed correctly, the chosen card will always be eleventh

    restart_game = input("Do you want to play again, press '1' for yes and '2' for no")
    if restart_game == "1":
        main()
    else:
        exit
        
main()

# references
# http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console
