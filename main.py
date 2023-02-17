# This is a sample Python script.
#Module 5

#Review Questions for Chapter 5
#1) What is the difference between a tuple and a list?
#The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are
#mutable. Therefore, it is possible to change a list but not a tuple. The contents of a tuple cannot change once
# they have been created in Python due to the immutability of tuples.
#Assignment changes variables, but mutation changes objects. Most Python objects can be changed after they've been
# created. Lists, sets, and dictionaries can all be changed, whereas tuples, numbers, and strings cannot.






#2) How is a list different than a dictionary?
#A list is an ordered sequence of objects, whereas dictionaries are unordered sets. However, the main difference
# is that items in dictionaries are accessed via keys and not via their position.
#Dictionary is a key and does not have an order but you cannot use same words twice.






#3) Create a program that prints a list of words in random order. The program should print all the words and
# not repeat any.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random
list = ["one", "two", "three", "four"]
reap = []
while len(list) !=len(reap):
    #pick one word at random
    word = random.choice(list)
    if word not in reap:
        print(word)
        reap.append(word)
        #append is a modifier





# 4) Write a Character Creator program for a role-playing game. The player should be given a pool of 30 points to
# spend on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able to spend points
# from the pool on any attribute and should also be able to take points from an attribute and put them back into
# the pool.
#
#totalpoints=30
#characters={}
#choice= None
#while choice !="0":
#    print(
#        """
#        1. Create a new characters
#        2. Allocate Points
#        3. Deallocate Points
#        0. Exit
#        """
#    )
#choice = str(input("Enter your choice: "))
##if choice == "1":
#    characterName = input("Enter the character name: ")
#    if characterName not in characters:
#        characters[characterName]={"Strength":0, "Health":0, "Wisdom":0, "Dexterity":0}
#    else:
#        print("Character already exists!")
#elif choice == "2":
#    print("Characters are: ")
#    for character in characters:
#        print(character)
#        characterName = input("What character you want to allocate points to? ")
#        if characterName not in characters:
#            print("Character doesn't exist")
#        else:
#            attribute = input("Allocate the points to which one: Strength, Health, Wisdom or Dexterity? ")
#            if attribute not in characters [characterName]:
#                print("Invalid attribute!!")
#            else:
#                remainingPoints = totalpoints - sum([characterName[k] for k in characters [characterName]])
#                points = int(input("Enter the number of points to allocate to %s:"%attribute))
#                if points > remainingPoints:
#                    print("Given points exceed the remaining points!!")
#                else:
##                    characters[characterName][attribute] += points
#                   print(characters[characterName])
#elif choice == "3":
#            print("Characters are:")
#            for character in characters:
#                print(character)
#                characterName = input("What character do you want to deallocate points? ")
#                if characterName not in characters:
#                    print("Character doesn't exist")
#                else:
#                    attribute = input("Deallocate points from Strength, Health, Wisdom, or Dexterity)?")
#                    if attribute not in characters[characterName]:
#                        print("Invalid attribute!!")
#                    else:
#                        allocatedpoints = characters[characterName][attribute]
#                        points = int(input('Enter the number of points to deallocate to %s:'%attribute))
#                        if points > allocatedpoints:
#                            print("points can't be less than the allocated points!")
#                        #else:
#                            #characters[characterName][attribute] -= points
#                            #print(characters[characterName])
#elif choice == "0":
    #print("goodbyeeee")
    #else:
#    print("not correct!!")







# 5) Write a Who’s Your Daddy? program that lets the user enter the name of a male and produces the name of
# his father. (You can use celebrities, fictional characters, or even historical figures for fun.) Allow the user
# to add, replace, and delete son-father pairs.

#Pick = None
#Daddy = {}

#loop
#while Pick != "0":
    #print choices
#    print(
#        """
#        1. Enter the name of a male.
#        2.ADD PAIR
#       #3. REPLACE PAIR
#      4. Delete a father-son pair.
 #       """
#    )
#ask user chioces
#    Pick = input("What do you want to do? ")
#    if Pick== "1":
#        #name of son
#        son = input("Enter Son's name: ")
#        #check to see if pair exists
#        if son in Daddy:
#            print("Father of %s is %s" % (son, Daddy[son]))
#        else:
#            print("There is no info on this person!!")
#    elif Pick== "2":
#        son = input("Enter Son's name: ")
#        if son not in Daddy:
#            father = input("Enter name of father: ")
#            Daddy[son] = father
#    else:
#        print("Pair already exists!!")
#    elif Pick == "3":
#            son = input("Enter Son's name: ")
#        in son not in Daddy:
#            son = input("Enter Son's name: ")
#
 #   if son in Daddy:
  #  father = input("Replace father's name: ")
   #         Daddy[son] = father
    #    else:
     #       print("Paid does not exist")
#    elif Pick== "4":
 #           son = input("Enter Son's name: ")
  #      if son in Daddy:
   #         del Daddy[son]
    #    else:
     #       print("Pair does not exist!")

    #else:
     #   print("Wrong answer")