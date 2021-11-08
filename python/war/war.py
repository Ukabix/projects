# GLOBALS
# random library for card shuffling
import random

# define card suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# define card ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# define card values to compare them in game logic later
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# CARD
# must have those attributes: SUIT,RANK,VALUE


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  # recall values dictionary by key = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# DECK
# 1) create a new deck:
# create 52 Card objects
# hold them as a list of Card objects
# 2) Shuffle a deck
# use shuffle() method form random
# 3) deal cards from Deck
# pop method from Card list


class Deck:
    # create a list of Card objects
    def __init__(self):
        self.all_cards = []  # create an empty list of all cards

        for suit in suits:  # iterate through suits
            for rank in ranks:  # iterate through ranks
                # create Card object
                created_card = Card(suit, rank)
                # append created cards to Card list
                self.all_cards.append(created_card)
        # to check if it works run
        # for card_object in new_deck.all_cards:
        #   print(card_object)
    # implement shuffling

    def shuffle(self):
        random.shuffle(self.all_cards)
        # to check if it works run
        # for card_object in new_deck.all_cards:
        #   print(card_object)
    # deal one card function

    def deal_one(self):
        return self.all_cards.pop()
        # to check if it works run
        # new_deck = Deck()
        # new_deck.shuffle()
        # mycard = new_deck.deal_one()
        # print(mycard)
        # len(new_deck.all_cards) == 51

# PLAYER
# 1) holds player's list of cards
# 2) should be able to add or remove cards from the list of Card objects
# 3) add 1 or more cards to the list
# 4) translate a deck/hand of cards with a top and bottom to a list
# player plays a card: pop(0)
# player adds a card: append() - be default to the end of list
# player adds multiple cards: extend(new)


class Player:
    def __init__(self, name):
        self.name = name  # distinguish players
        self.all_cards = []  # create empty hand

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # for multiple cards -> new_cards is a list
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # single card -> new_cards is a single obj
        else:
            self.all_cards.append(new_cards)
        # to check:
        # new_player = Player("John")
        # print(new_player) -> expect 0
        # new_player.add_cards(mycard)
        # print(new_player) -> expect 1
        # print(new_player.all_cards[0])
        # for multiple:
        # new_player.add_cards([mycard,mycard,mycard]) etc.

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

# GAME LOGIC
# outline:
# card dealing:
# 1. create two player classes
# 2. create a new deck
# 3. shuffle the deck
# 4. split the deck between players
# playing:
# 1. lose check for less than 5 cards -> game_on = False: end game, win information
# 2. while game_on = True:
# 3. each player draws
# 4. compare cards -> card1 != card2 -> at_war = False
# 5. while at_war = True
# 6. players draw five additional cards, back to 4.
# 7. add cards to winner, back to 1.


# GAME SETUP
# create player1
player_one = Player("one")
# create player2
player_two = Player("two")
# create new deck
new_deck = Deck()
# shuffle new deck
new_deck.shuffle()
# split the deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
# test: len(plyer_one.all_cards) -> expect 26

# GAME START
game_on = True
# count rounds
round_num = 0
# WHILE GAME_ON
while game_on:

    round_num += 1
    print(f"Rounds {round_num}")

    # game over check
    if len(player_one.all_cards) == 0:
        print("Player One is out of cards. Player Two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards. Player One wins!")
        game_on = False
        break

    # START A NEW ROUND
    # select cards to play
    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    # CARD COMPARISON
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print("Player one has won this one.")
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_one_cards)
            print("Player two has won this one.")
            at_war = False
        else:
            # at_war
            print("WAAAGH!")
            if len(player_one.all_cards) < 5:
                print("Player one is unable to go to war. Player two wins!")
                game_on = False
                break
            if len(player_two.all_cards) < 5:
                print("Player two is unable to go to war. Player one wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
