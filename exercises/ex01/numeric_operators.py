"""Numeric Operators Exercise."""
__author__ = "730407263"

num1: int = int(input("Left-hand side: "))
num2: int = int(input("Right-hand side: "))
num3: int = num1 ** num2
num4: float = num1 / num2
num5: int = num1 // num2
num6: int = num1 % num2

print(str(num1) + " ** " + str(num2) + " is " + str(num3))
print(str(num1) + " / " + str(num2) + " is " + str(num4))
print(str(num1) + " // " + str(num2) + " is " + str(num5))
print(str(num1) + " % " + str(num2) + " is " + str(num6))