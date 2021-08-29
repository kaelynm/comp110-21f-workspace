"""Relatioinal Operators Exercise."""
_author_ = str(730407263)

num1: int = int(input("Left-hand side: "))
num2: int = int(input("Right-hand side: "))
num3: bool = num1 < num2
num4: bool = num1 >= num2
num5: bool = num1 == num2
num6: bool = num1 != num2

print(str(num1) + " < " + str(num2) + " " + str(num3))
print(str(num1) + " >= " + str(num2) + " " + str(num4))
print(str(num1) + " == " + str(num2) + " " + str(num5))
print(str(num1) + " != " + str(num2) + " " + str(num6))
