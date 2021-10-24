## do poprawy - coś jest nie tak z f palindrome

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# definicje funkcji


def palindrome(word):
    word2 = word[::1]
    return word2


def menu():
    print("Welcome. This program will determine if the word you input is a palindrome")
    print("Please enter your selection")
    print("1. Run program")
    print("2. Credits")
    print("3. Quit")
    return input("Choose 1-3")


def main():
    answer = ""
#    palindrome = ""
    choice = ""
    while choice != "3":
        choice = menu()
        if choice == "1":
            word = str(input("Please input your word:"))
            if palindrome != word:
                print("y")
            else:
                print("n")
            print(word)
            print(palindrome)
#           if palindrome == True:
#                answer == ("Yay, ", word, "is a palindrome, good job!")
#                print("y")
#            else:
#                print("n")
#                answer == ("Unfortunately ", word, "is not a palindrome.")
        elif choice == "2":
            print("2019, ŁP")
        elif choice == "3":
            break
#        else:
#            print("")
        if answer != "":
           print(answer)


main()

# word = ""
# while True:
#    word = input("Please input a word: ")
#    palindrome = word[::1]
#    if word == palindrome
#       print(word, "is a palindrome ->", palindrome)

#    return True
