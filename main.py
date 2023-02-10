#Module 4
#Review Questions for Chapter 4
#1. What is a variable?
#It is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can
# refer to the object by that name.
#
#2 What is a constant?
#the term constant refers to names representing values that don't change during a program's execution. A constant is a
# type of variable that holds values, which cannot be changed. In reality, we rarely use constants in Python. Constants
# are usually declared and assigned on a different module/file. Then, they are imported to the main file. Variables are
# mutable, i.e., their values can be changed and updated. Constants are immutable, i.e. their values cannot be changed
# or updated. Literals are both mutable or immutable depending on the type of literal used.
#
#3. Can a variable be changed once assigned?
#Some values in python can be modified, and some cannot. This does not ever mean that we can't change the value of a
# variable – but if a variable contains a value of an immutable type, we can only assign it a new value. We cannot alter
# the existing value in any way.#
#
#4. Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount
# by which to count.
#start = int(input(“Enter a starting a number: “))
#end = int(input(“Enter an ending number: “))
#amount = int(input (“Enter an amount by which to count in spaces: “))
#For i in in range (start,end+=1, amount):
#Print(i)


#5. Create a program that gets a message from the user and then prints it out backwards.

Message = input(“Enter a message: ”)
Print(“Printing it out backwards: )
Print(message[::-1])
# this is how words get typed backwards on coding, like a secret code



#6. Create a game where the computer picks a random word and the player has to guess that word. The computer tells the
# player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The
# computer can only respond with “yes” or “no”. Then, the player must guess the word.

# The computer picks a random word
# The computer tells player how many letter. five chances, player has to guess the original word

#import random
# create a sequence of words to choose from
#WORDS = ("sun", "is", "up", "little", "after", "twelve")
# pick one word randomly from the sequence

#word = random.choice(WORDS)
#print ("How many letters are in the word? ", len(word))
#guess = 0
#typed = " "
# create five chances to guess letter of the word
#while guess <5:
#    letter = input ("Guess a letter in the word: ")
#    if letter in word:
#        print("yes")
#    elif letter not in word:
#     print ("nope")
#    guess +=1
#print("You must guess the word now: ")
# player types word
#typed = input("The word: ")
#Guessed correctly
#if typed.lower == word:
#    print("That's it!  You guessed it!")
#Guessed incorrectly
#elif typed.lower != word and word != "":
#    print("Sorry, that's not it.")
