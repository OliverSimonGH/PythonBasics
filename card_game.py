import random, os

#Clears the cmd prompt for multiple operating systems.
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    #Variables I used within the cored to store data.
    #First three variable used to create and store a deck of cards.
    card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_list_52 = []

    #Used to get 21 cards from the deck of cards.
    card_list_21 = []

    #These three lists are to store each individual row, so they can be manipualted and displayed.
    row_one = []
    row_two = []
    row_three = []

    #This list is used to store the deck with the chosen card in the middle.
    middle_deck = []

    #When a row is picked, this section will put the selected row inbetween the other two rows.
    def pick_a_row():
        #User inputs either 1, 2 or 3.
        input_answer = input("What row is your card in (1)(2)(3): ")
        #if 1 is selected then execute code below, same goes for 2 and 3.
        if input_answer == "1":
            #Puts the row selected in the middle of other two rows, and store it in middle_deck list, same goes for 2 and 3.
            middle_deck.extend(row_two + row_one + row_three)
        elif input_answer == "2":
            middle_deck.extend(row_one + row_two + row_three)
        elif input_answer == "3":
            middle_deck.extend(row_one + row_three + row_two)
        else:
            #If 1, 2 or 3 are not chosen, the function while loop due to recursion.
            pick_a_row()

    #This will clear each individual row so they be used again in the section below.
    def clear_row():
        row_one.clear()
        row_two.clear()
        row_three.clear()

    #This will shuffle the cards by putting the cards in a row 1 at a time row by row and not column by column.
    def shuffle():
        while len(middle_deck) > 0:
            #Adds the first card of middle_deck to row one
            row_one.append(middle_deck[0])
            #Removes the first card from the middle deck, so this process can be sued with another row.
            middle_deck.remove(middle_deck[0])

            #Same happens here as it did above, instead of row one, it happens to row two.
            row_two.append(middle_deck[0])
            middle_deck.remove(middle_deck[0])

            row_three.append(middle_deck[0])
            middle_deck.remove(middle_deck[0])

        #When cards have been shuffled, each row will get printed out on different lines.
        print("\nRow one: {} \nRow two: {} \nRow three: {}".format(row_one, row_two, row_three))

    #creating a deck of cards.
    for i in card_numbers:
        for o in card_suit:
            #Adding the suit and number together to create individual cards.
            card_list_52.append(i + " of " + o)

    #randomly select 21 card from the deck of cards.
    while len(card_list_21) < 21:
        #Gets a random cards from the deck and store it in a varibale.
        card = random.choice(card_list_52)
        #Adds the random cards to card_list_21 list.
        card_list_21.append(card)
        #Removes that card so it cannot be selected again, meaning no cards are the same.
        card_list_52.remove(card)

    #Creates three different rows from the deck of 21 cards, these rows of 7 are used for the magic trick.
    while len(row_three) != 7:
        #Assigns 7 cards to each row.
        row_one.extend(card_list_21[:7])
        row_two.extend(card_list_21[7:14])
        row_three.extend(card_list_21[14:21])

    #Prints out the cards in rows once they have been created.
    print("Row one: {} \nRow two: {} \nRow three: {}".format(row_one, row_two, row_three))

    #Calling the functions to play the game.
    pick_a_row()
    clear_row()
    shuffle()

    pick_a_row()
    clear_row()
    shuffle()

    # Put the cards in the middle_deck list so the eleventh card can be chosen.
    pick_a_row()

    #grab the the eleventh card in the middle deck.
    print("\nYour answer is: {}".format(middle_deck[10]))

    #Prompts user to play again.
    restart_game = input("Do you want to play again, press '1' for yes and '2' for no\n")
    #If the user enters 1, then the code below execututes.
    if restart_game == "1":
        #Calls function clear_screen() to clear all the text on the command propmt
        clear_screen()
        #Calls function main() which will restart the game.
        main()
    else:
        #If anything other than 1 is entered, the game will exit.
        exit

#Runs the game.
clear_screen()
main()

#references
# rubenvb (2015) How to clear python interpreter console. Available at: http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console (Accessed: 2 November 2016).
# 2016, Python Official Docs (no date) Data structures — python 3.5.2 documentation. Available at: https://docs.python.org/3/tutorial/datastructures.html (Accessed: 1 November 2016).
# What is the syntax to insert one list into another list in python? (2010) Available at: http://stackoverflow.com/questions/3748063/what-is-the-syntax-to-insert-one-list-into-another-list-in-python (Accessed: 3 November 2016).
# Explain python’s slice notation (2016) Available at: http://stackoverflow.com/questions/509211/explain-pythons-slice-notation (Accessed: 7 November 2016).
