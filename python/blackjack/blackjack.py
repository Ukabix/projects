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
        self.deck = [] # create initial empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # append created cards to Card list
    # string representation of deck
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # iterate through string representations of card objects
        return "The deck has: " + deck_comp
    # shuffling func
    def shuffle(self):
        random.shuffle(self.deck)
    # dealing funct
    def deal(self):
        single_card = self.deck.pop() # grab 1st card from deck list and set it as single_card
        return single_card

# Hand Class
class Hand():
    # init
    def __init__(self):
        self.cards = [] # create initial empty list
        self.value = 0 # create initial hand value
        self.aces = 0 # create initial attrib to track aces
    # add card func
    def add_card(self,card):
        self.cards.append(card) # card passed from deck.deal() func
        self.value += values[card.rank] # add to hand value, from value dict - card rank as key
        # testing:
        # test_deck = Deck()
        # test_deck.shuffle()
        # PLAYER
        # test_player = Hand()
        # pulled_card = test_deck.deal # deal 1 card from deck
        # print(pulled_card)
        # test_player.add_card(pulled_card)
        # print(test_player.value)
        # shorter ver test_player.add_card(test_deck.deal())
        # test_player.value

        # track aces
        if card.rank == "Ace":
            self.aces += 1

    # ace value adj func
    def adjust_for_ace(self):
        # if total val > 21  and I still have an ace
        # change my ace value from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Chips class
class Chips:
    def __init__(self):
        self.total = 100 # default
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

# GAMEPLAY FUNCTIONS
# Take bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How mny chips ould you like to bet?"))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips. You have: {}".format(chips.total))
            else:
                break

# Hit
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

# Hit or stand
def hit_or_stand(deck,hand):
    global game_on # to control the game loop
    while True:
        x = input("Hit or Stand? Enter h or s.")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lowercase() == 's':
            print("Player stands. Dealer's turn.")
            game_on = False
        else:
            print("Sorry, wrong input, please type 'h' or 's'.")
            continue
        break

# display card functions
# starting view
def show_some(player,dealer):
    # show only 1 of dealer's cards - dealer.cards[0,1]
    print("\n Dealer's hand: ")
    print("First card is hidden.")
    print(dealer.cards[1])
    # show all (2 cards) of player's cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)

# end view
def show_all(player,dealer):
    # show all dealer's cards
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    # calculate and display value
    print(f"Dealer hand value: {dealer.value}.")

    # show all player's hands
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    # calculate value
    print(f"Player hand value: {player.value}.")

# game over functions
def player_busts(player,dealer,chips):
    print("Player bust!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer bust!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player have a draw. Push!")

# GAME LOGIC
while True:
    # Print an opening statement
    print("Welcome to Blackjack!")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal)
    player_hand.add_card(deck.deal)

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal)
    dealer_hand.add_card(deck.deal)
            
    # Set up the Player's chips
    player_chips = Chips()
        
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while game_on:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        # Show all cards
        show_all(player_hand,dealer_hand)    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    # Inform Player of their chips total
    print("\n Player total chips are at: {}".format(player_chips.total))
    # Ask to play again
    new_game   = input("Would you like to play again? y/n")
    if new_game[0].lower() == 'y':
        game_on = True
        continue
    else:
        print("Thanks for playing!")
        break
