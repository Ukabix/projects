## Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right.
# Extras:
#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random
a = random.randint(1, 9)
print(a) #spr

# v.1
# def main():
#        while True:
#        guess = int(input("Please guess the number: "))
#        if guess == a:
#            print("That is right! Congrats!")
#        if guess < a:
#            print("You guessed wrong. The random number is larger.")
#        if guess > a:
#            print("You guessed wrong. The random number is smaller.")
# main()

# v.2
def main():
    counter = 0
    while counter >= 0 or guess != exit:
        guess = input("Please guess the number or type 'exit' to quit: ")
        if guess == "exit":
            print("Goodbye!")
            break
        #guess = int(guess)
        if int(guess) < a:
            counter += 1
            print("You guessed wrong. The random number is larger. This is your ", counter, " try")
        elif int(guess) > a:
            counter += 1
            print("You guessed wrong. The random number is smaller. This is your ", counter, " try")
        elif int(guess) == a:
            counter += 1
            print("That is right! You guessed on your ", counter, " try. Congrats!")
        else:
            print("Please give a valid input")




#        elif guess == "exit":
#            break
#        elif guess.isnumeric():
#            print("Please input a number or 'exit' command")

main()

# może dodać jeszcze reset licznika? 
# zrobić program, który sam obliczy rn?
