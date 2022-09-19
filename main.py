import os
import random
import pandas as pd

def outputFormating(toShow):
    
    for i in range(len(toShow)):

        print("{}.".format(i+1))
        print("     Name:   {}".format(toShow[i][0]))

        aux = toShow[i][1][0]
        
        if len(toShow[i][1]) > 1:

            for j in range(1, len(toShow[i][1])):
                aux = aux + ", " + toShow[i][1][j]

        print("     Genre:  {}".format(aux))
        print("     Type:   {}".format(toShow[i][2]))
        print("     Length: {}, {}".format(toShow[i][3][0], toShow[i][3][1]))



os.system("clear")

print("****************************")
print("*                          *")
print("*       ANIME PICKER       *")
print("*                          *")
print("****************************")


# List of animes
animes = [["5 Centimeters Per Second", ["Drama", "Romance", "Slice of Life"], "Movie", ["Short", "1h06"]], 
            ["Ponyo", ["Adventure", "Fantasy"], "Movie", ["Short", "1h40"]], 
            ["Your Name.", ["Drama", "Supernatural"], "Movie", ["Short", "1h46"]], 
            ["The Garden of Words", ["Drama", "Romance", "Slice of Life"], "Movie", ["Short", "0h46"]], 
            ["Hakubo", ["Romance"], "Movie", ["Short", "0h52"]],
            ["Black Clover", ["Action", "Comedy", "Fantasy"], "Series", ["Long", "1 Season (170)"]], 
            ["Gokushufudou", ["Comedy"], "Series", ["Short", "2 Seasons (5/5)"]], 
            ["K-On!", ["Comedy"], "Series", ["Short", "2 Seasons (13/26)"]], 
            ["Kuroko no Basket", ["Sports"], "Series", ["Long", "3 Seasons, 1 Movie (25/25/25/1h30)"]], 
            ["How Not to Summon a Demon Lord", ["Comedy", "Fantasy", "Ecchi"], "Series", ["Short", "2 Seasons (12/10)"]]
         ]



choice = 0

print("\nChoose an option:")

while choice < 1 or choice > 2:

    print("1. Select random anime")
    print("2. Filter")

    choice_string = input("\nYour choice: ")

    choice = int(choice_string)

    if choice < 1 or choice > 2:
        os.system("clear")
        print("Please, select one of the available options!!\n\n")

os.system("clear")

if choice  == 1:
    temp = random.randint(0, len(animes)-1)
    toShow = []
    toShow.append(animes[temp])

    print("The selected anime is:")

    outputFormating(toShow)
    print("\nENJOY IT!")
    exit()


# List of filters
filters = ["Genre", "Series/Movie", "Length"]


# Creating a list of genres
genres_duplicates = []

for anime in animes:

    for i in range(len(anime[1])):

        genres_duplicates.append(anime[1][i])


# Erasing genres duplicates
genres = []

genres.append(genres_duplicates[0])

for i in range(1, len(genres_duplicates)):

    duplicate = False

    for genre in genres:

        if genres_duplicates[i] == genre:
            duplicate = True
            break
    
    if not duplicate:

        genres.append(genres_duplicates[i])
        


# Choosing filter option
choice = 0

print("\nChoose a filter option:")

while choice < 1 or choice > len(filters):

    for i in range(len(filters)):
        print("{}. {}".format(i+1, filters[i]))

    choice_string = input("\nYour choice: ")

    choice = int(choice_string)

    if choice < 1 or choice > len(filters):
        os.system("clear")
        print("Please, select one of the available options!!\n\n")


# Filter options funtionality

os.system("clear")

# Genre chooser
if choice == 1:

    filterTag = "genre"

    choice = 0

    print("Choose a genre:")
    
    while choice < 1 or choice > len(genres):

        for i in range(len(genres)):
            print("{}. {}".format(i+1, genres[i]))

        choice_string = input("\nYour choice: ")

        choice = int(choice_string)

        if choice < 1 or choice > len(genres):
            os.system("clear")
            print("Please, select one of the available genres!!\n\n")



# Series/Movie chooser
elif choice == 2:

    filterTag = "type"

    choice = 0
    
    print("Choose one of the following:")

    while choice < 1 or choice > 2:

        print("1. Series")
        print("2. Movie")

        choice_string = input("\nYour choice: ")

        choice = int(choice_string)

        if choice < 1 or choice > 2:
            os.system("clear")
            print("Please, select one of the available options!!\n\n")

    

elif choice == 3:

    filterTag = "length"

    choice = 0
    
    print("Choose your prefered length:")

    while choice < 1 or choice > 2:

        print("1. Short (-50 episodes and films)")
        print("2. Long (+50 episodes)")

        choice_string = input("\nYour choice: ")

        choice = int(choice_string)

        if choice < 1 or choice > 2:
            os.system("clear")
            print("Please, select one of the available length!!\n\n")



os.system("clear")


if filterTag == "genre":

    toShow = []

    print("This is a list of the animes categorized as {}:".format(genres[choice-1]))

    for anime in animes:
        
        for i in range(len(anime[1])):

            if genres[choice-1] == anime[1][i]:
                toShow.append(anime)
                break

    outputFormating(toShow)

    
elif filterTag == "type":

    toShow = []

    if choice == 1:
        print("This is a list of the anime series:")
    else:
        print("This is a list of the anime movies")

    for anime in animes:

        if  choice == 1:
            if "Series" == anime[2]:    
                toShow.append(anime)
            
        else:
            if "Movie" == anime[2]:
                toShow.append(anime)


    outputFormating(toShow)

    
elif filterTag == "length":

    toShow = []

    if choice == 1:
        print("This is a list of short animes:")
    else:
        print("This is a list of long animes:")

    for anime in animes:

        if  choice == 1:
            if "Short" == anime[3][0]:    
                toShow.append(anime)
            
        else:
            if "Long" == anime[3][0]:
                toShow.append(anime)


    outputFormating(toShow)


answer = "a"

while not answer.lower().startswith("y") and not answer.lower().startswith("n"):

    answer = input("\nDo you want to select one randomly?: ")

    if answer.lower().startswith("y"):
        temp = random.randint(0, len(toShow)-1)
        toShow = []
        toShow.append(animes[temp])

        os.system("clear")

        print("The selected anime is:")

        outputFormating(toShow)
        print("\nENJOY IT!")

    elif answer.lower().startswith("n"):
        os.system("clear")
        print("\nHave a grate day!")

    else:
        os.system("clear")
        print("Please, just write Yes or No!\n")