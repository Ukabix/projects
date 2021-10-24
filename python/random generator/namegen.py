import csv
import random

### define basic functions
## male
def give_male_data():
# listing names
    imiona = []
    with open('imionameskie.csv', encoding= 'utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            imiona.append(row)
        # print(imiona)
# listing surnames
    nazwiska = []
    with open('imionameskie.csv', encoding= 'utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            nazwiska.append(row)
    # print(nazwiska)
    imie= random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    print(imie, ' ', nazwisko)
give_male_data()

## female
def give_female_data():
# listing names 
    imiona = []
    with open('imionazenskie.csv', encoding= 'utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            imiona.append(row)
        # print(imiona)
    # listing surnames
    nazwiska = []
    with open('imionameskie.csv', encoding= 'utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            nazwiska.append(row)
        # print(nazwiska)
    imie= random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    print(imie, ' ', nazwisko)
give_female_data()