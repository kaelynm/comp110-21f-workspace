"""Repeating a beat in a loop."""

__author__ = "730407263"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
count: int = 0 
output: str = ""

if repeat > 0:
    while count < repeat:
        output = output + beat
        count = count + 1
        if count < repeat:
            output = output + " "
else:
    output = "No beat..."

print(output)