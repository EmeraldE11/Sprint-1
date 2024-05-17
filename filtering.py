import numpy as np
import pandas as pd

df = pd.read_csv("gamearchive\games.csv")
names = ["Title", "Release Date", "Team", "Rating", "Times Listed", "Number of Reviews", "Genres", "Summary", "Reviews", "Plays", "Playing", "Backlogs", "Wishlist"]

def main() :
    usecols = column_list()

    will_sort = input("By default, the data is sorted by popularity.\nWould you like it to be sorted a certain column's metric instead?\nType n for No, y for Yes\n")
    if will_sort == "y":
        target = sort(usecols)
        ascend = order(target)
        display(usecols, target, ascend)
    elif will_sort == "n":
        display(usecols)
    else:
        print("That isn't a valid input. Please enter either n or y.")
        quit()


def column_list() :

    try:
        cols = int(input(f"How many columns do you want to include? Insert a number between 1 and 13\n"))
    except ValueError:
        print("That isn't a valid input. Please put a number between 1 and 13.")
        quit()
    if cols < 1 or cols > 13:
        print("That isn't a valid input. Please put a number between 1 and 13.")
        quit()
    usecols = []
    
    if cols != 13:
        print(f"Please select columns to include from this list. Input is case sensitive.\n1. Title           2. Release Date         3. Teams      4. Rating\n5. Times Listed    6. Number of Reviews   7. Genres     8. Summary\n9. Reviews          10. Plays              11. Playing\n12. Backlogs         13. Wishlist")
        for c in range(cols):
            try:
                title = int(input("Enter the number of a column: "))
            except ValueError:
                print("That isn't a valid input. Please put a number between 1 and 13.")
                quit()
            if title < 1 or title > 13:
                print("That isn't a valid input. Please put a number between 1 and 13.")
                quit()
            usecols.append(names[title - 1])
        return usecols
    else:
        return names

def sort(columns) :
    try:
        target = int(input(f"Please select the column you wish to sort by. Type the number of the column.\n1. Title           2. Release Date         3. Teams      4. Rating\n5. Times Listed    6. Number of Reviews   7. Genres     8. Summary\n9. Reviews          10. Plays              11. Playing\n12. Backlogs         13. Wishlist\n"))
    except ValueError:
        print("That isn't a valid input. Please put a number between 1 and 13.")
        quit()
    if target < 1 or target > 13:
        print("That isn't a valid input. Please put a number between 1 and 13.")
        quit()
    true_target = names[target - 1]
    return true_target

def order(target) :
    if target == "Release Date" :
        print("This program isn't cool enough to sort by date, sorry.")
    elif target == "Title" or target == "Teams" or target == "Genres" or target == "Summary" or target == "Reviews" :
        ascending = input(f"Do you want this column sorted A-Z (True) or Z-A (False)?\n")
        if ascending == "True":
            ascending = True
            return ascending
        elif ascending == "False":
            ascending = False
            return ascending
        else:
            print("That isn't a valid input. Please type exactly True or False.")
            quit()
    else:
        ascending = input(f"Do you want this column sorted Low-High (True) or High-Low (False)?\n")
        if ascending == "True":
            ascending = True
            return ascending
        elif ascending == "False":
            ascending = False
            return ascending
        else:
            print("That isn't a valid input. Please type exactly True or False.")
            quit()

def display(columns, sort = "no", ordering = "no") :
    try:
        count = int(input("How many data entries do you want shown? (Enter a number between 1 and 1512.)\n"))
    except ValueError:
        print("That isn't a valid input. Please put a number between 1 and 13.")
        quit()
    if count == 0:
        df = pd.read_csv("gamearchive\games.csv", usecols=columns)
        print(f"{df}")
        quit()
    elif count < 1 or count > 1512:
        print("That isn't a valid input. Please put a number between 1 and 1512.\n(Enter 0 if you want all of the data.)\n")
        quit()
    
    df = pd.read_csv("gamearchive\games.csv", usecols=columns)

    if sort == "no" and ordering == "no":
        print(f"{df.head(count)}")
    #extra options because of ordering?
    elif sort == "no":
        df = df.sort_values(ascending=ordering)
        print(f"{df.head(count)}")
    elif ordering == "no":
        df = df.sort_values(sort)
        print(f"{df.head(count)}")
    else: 
        df = df.sort_values(sort, ascending=ordering)
        print(f"{df.head(count)}")

main()