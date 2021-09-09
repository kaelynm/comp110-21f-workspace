"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730407263"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
fortune = randint(1, 4)
if fortune < 3:
    if fortune == 1:
        print("A fresh perspective is coming your way")
    else:
        print("Hard work pays off in the future")
else:
    if fortune == 3:
        print("Change can hurt, but it creates a path to something better")
    else:
        print("Enjoy companionship")

print("Now, go spread positive vibes!")