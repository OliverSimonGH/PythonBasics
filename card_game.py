import random, os

#Clears the cmd prompt for multiples operating systems.
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    #Variables I used within the cored to store data.
    card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_list_52 = []
    card_list_21 = []
    row_one = []
    row_two = []
    row_three = []
    middle_deck = []

    #When a row is picked, this section will put the selected row inbetween the other two rows.
    def pick_a_row():
        input_answer = input("What row is your card in (1)(2)(3): ")
        if input_answer == "1":
            middle_deck.extend(row_two + row_one + row_three)
        elif input_answer == "2":
            middle_deck.extend(row_one + row_two + row_three)
        elif input_answer == "3":
            middle_deck.extend(row_one + row_three + row_two)
        else:
            pick_a_row()

    #This will clear each individual row so they be used again in the section below.
    def clear_row():
        row_one.clear()
        row_two.clear()
        row_three.clear()

    #This will shuffle the cards by putting the cards in a row 1 at a time row by row and not column by column.
    def shuffle():
        while len(middle_deck) > 0:
            card = middle_deck[0]
            row_one.append(card)
            middle_deck.remove(card)

            card = middle_deck[0]
            row_two.append(card)
            middle_deck.remove(card)

            card = middle_deck[0]
            row_three.append(card)
            middle_deck.remove(card)
        print("\nRow one: {} \nRow two: {} \nRow three: {}".format(row_one, row_two, row_three))

    #creating a deck of cards.
    for i in card_numbers:
        for o in card_suit:
            card_list_52.append(i + " of " + o)

    #randomly select 21 card from the deck of cards.
    while len(card_list_21) < 21:
        card = random.choice(card_list_52)
        card_list_21.append(card)
        card_list_52.remove(card)

    #Creates three different rows from the deck of 21 cards, these rows of 7 are used for the magic trick.
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

    #Calling the functions to play the game.
    pick_a_row()
    clear_row()
    shuffle()

    pick_a_row()
    clear_row()
    shuffle()

    # Put the cards in the middle_deck list.
    pick_a_row()

    #grab the the eleventh card in the middle deck.
    print("\nYour answer is: {}".format(middle_deck[10]))

    #Prompts user to play again.
    restart_game = input("Do you want to play again, press '1' for yes and '2' for no\n")
    if restart_game == "1":
        clear_screen()
        main()
    else:
        exit

#Runs the game.
clear_screen()
main()

#references
#rubenvb (2015) How to clear python interpreter console. Available at: http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console (Accessed: 2 November 2016).
#2016, Python Official Docs (no date) Data structures — python 3.5.2 documentation. Available at: https://docs.python.org/3/tutorial/datastructures.html (Accessed: 1 November 2016).
#What is the syntax to insert one list into another list in python? (2010) Available at: http://stackoverflow.com/questions/3748063/what-is-the-syntax-to-insert-one-list-into-another-list-in-python (Accessed: 3 November 2016).
