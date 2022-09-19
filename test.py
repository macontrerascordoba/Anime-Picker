from calendar import c
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import os
import random
import pandas as pd



def outputFormating(df_aux):

    temp = random.randint(0, df_aux.shape[0]-1)
    df_toShow = pd.DataFrame(columns = ["Name", "Genre", "Type", "Length"])

    name = df_aux.loc[temp, "Name"]
    genre = df_aux.loc[temp, "Genre"]
    aType = df_aux.loc[temp, "Type"]
    length = df_aux.loc[temp, "Length"]

    df_toShow = df_toShow.append({"Name" : name,
                     "Genre" : genre,
                     "Type" : aType,
                     "Length" : length
                    }, ignore_index = True)
        
    name = df_toShow.loc[0, "Name"]
    genre = df_toShow.loc[0, "Genre"]
    aType = df_toShow.loc[0, "Type"]
    length = df_toShow.loc[0, "Length"]

    print("Name:   {}".format(name))

    aux = genre[0]
    
    if len(genre) > 1:

        for j in range(1, len(genre)):
            aux = aux + ", " + genre[j]

    print("Genre:  {}".format(aux))
    print("Type:   {}".format(aType))
    print("Length: {}, {}".format(length[0], length[1]))



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


df_animes = pd.DataFrame(animes, 
                        columns = ["Name", "Genre", "Type", "Length"])

choice = 0


# Random/Filter options
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

    print("Your random anime is")

    outputFormating(df_animes)
    
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

    print("\nChoose a genre:")
    
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
    
    print("\nChoose one of the following:")

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
    
    print("\nChoose your prefered length:")

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

    df_aux = pd.DataFrame(columns = ["Name", "Genre", "Type", "Length"])

    for i in range(df_animes.shape[0]):
        
        name = df_animes.loc[i, "Name"]
        genre = df_animes.loc[i, "Genre"]
        aType = df_animes.loc[i, "Type"]
        length = df_animes.loc[i, "Length"]

        for j in range(len(genre)):

            if genres[choice-1] == genre[j]:
                df_aux = df_aux.append({"Name" : name,
                                  "Genre" : genre,
                                  "Type" : aType,
                                  "Length" : length
                                 }, ignore_index = True )
                break


    print("Your random {} anime is:\n".format(genres[choice-1].lower()))

    outputFormating(df_aux)
    
    print("\nENJOY IT!")

    
elif filterTag == "type":

    df_aux = pd.DataFrame(columns = ["Name", "Genre", "Type", "Length"])

    for i in range(df_animes.shape[0]):
        
        name = df_animes.loc[i, "Name"]
        genre = df_animes.loc[i, "Genre"]
        aType = df_animes.loc[i, "Type"]
        length = df_animes.loc[i, "Length"]

        if  choice == 1 and "Series" == aType:
            df_aux = df_aux.append({"Name" : name,
                                  "Genre" : genre,
                                  "Type" : aType,
                                  "Length" : length
                                 }, ignore_index = True )
            
        elif choice == 2 and "Movie" == aType:
            df_aux = df_aux.append({"Name" : name,
                                  "Genre" : genre,
                                  "Type" : aType,
                                  "Length" : length
                                 }, ignore_index = True )

    if choice == 1:
        text = "series"
    
    if choice == 2:
        text = "movie"

    print("Your random anime {} is:\n".format(text))

    outputFormating(df_aux)
    
    print("\nENJOY IT!")