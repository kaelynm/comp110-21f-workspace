"""Counting letters in a string."""

__author__ = "730407263"


letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
counter: int = 0
num_letters: int = 0 

while len(word) > counter:
    if word[counter] == letter:
        num_letters = num_letters + 1
    counter = counter + 1

print("Count: " + str(num_letters))