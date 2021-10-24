import datetime

def nameloop():
    name = ""
    while True:
        name = input("please tell me your name")
        if not name.isalpha():
            print("That is not a name, please try again")
        else:
            print("Hello ", name, "!")
            break

def ageloop():
    age = ""
    yearnow = datetime.datetime.now().year
    while True:
        age = input("please tell me your age")
        if age.isdigit():
            ageint = int(age)
            year = yearnow + (100-ageint)
            print("Good news! You will turn 100 years old in", year)
            break
        else:
            print("Please enter a number!")


nameloop()
ageloop()

#Ewentualnie inny sposób na kiedy indziej - poprzez timedelta?
#age = input("please tell me your age")
#num = input("please give me a random number")
#day = int(input("please tell me the day you were born"))
#month = int(input("please tell me the month you were born"))
#year = int(input("please tell me the year you were born"))
#date1 = datetime.date(year, month, day)
#year, month, day = map(int, birthdate.split("-"))
#birthdate1 = datetime.date(year, month, day)
#print(year)
#print(month)
#print(day)
#age = timedelta(today, date1)


#print
#print("Today is ", today, "You were born on", date1)
#print("you are ", age, "years old")
#print("You will turn 100 in ")
