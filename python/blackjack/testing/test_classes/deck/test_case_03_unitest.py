# ASSIGNMENT
# Here are the requirements:

#     You need to create a simple text-based BlackJack game
#     The game needs to have one player versus an automated dealer.
#     The player can stand or hit.
#     The player must be able to pick their betting amount.
#     You need to keep track of the player's total money.
#     You need to alert the player of wins, losses, or busts, etc...

# And most importantly:

#     You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!

# Game Play

# To play a hand of Blackjack the following steps must be followed:

#     Create a deck of 52 cards
#     Shuffle the deck
#     Ask the Player for their bet
#     Make sure that the Player's bet does not exceed their available chips
#     Deal two cards to the Dealer and two cards to the Player
#     Show only one of the Dealer's cards, the other remains hidden
#     Show both of the Player's cards
#     Ask the Player if they wish to Hit, and take another card
#     If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
#     If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
#     Determine the winner and adjust the Player's chips accordingly
#     Ask the Player if they'd like to play again

# Playing Cards

# A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) 
# and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) 
# for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. 
# Aces have a rank of either 11 or 1 as needed to reach 21 without busting. 
# As a starting point in your program, you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.

# SOLUTION

# GLOBALS
# importing random for shuffle functionality
import random
# defining card characteristics and values for card objects
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11} # remember to handle Ace as 1 or 11
# declaring boolean for main game loop
game_on = True

# CLASSES
# Card Class
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] # recall values dictionary by key = rank
    # string representation of card
    def __str__(self):
        return self.rank + " of " + self.suit

# Deck Class
class Deck():
    # init
    def __init__(self):
        self.deck = [] # create an empty list of all cards
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # append created cards to Card list
    # string representation of deck
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # iterate through string representations of card objects
        return "The deck has: " + deck_comp
    # implement shuffling
    def shuffle(self):
        random.shuffle(self.deck)

    # dealing function
    def deal(self):
        single_card = self.deck.pop() # grab 1st card from deck list and set it as single_card
        return single_card

# test scenario: testing Deck class
# test case 03:
# white box deal fnc
# environment: venv Python 3.7.3 64 bit, VSC debug mode, W10 x64
# input data: test_deck object, test_card object, print() fnc
# expected result: radomised, shuffled list of 51 cards; single_card object
# 

test_deck = Deck()
test_deck.shuffle()
test_card = test_deck.deal()

print(test_deck)

print(len(test_deck.deck))

print(test_card)

# test build = master 08.11.2021
# test date = 08.11.2021
# test result = passed