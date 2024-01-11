import math
from typing import List

x: int = int(input("Enter first number :- "))
my_operator: List[str] = ["+", "-", "*", "/", "to pwr", "sqroot"]

for i, item in enumerate(my_operator, start=1):
    print("[", i, "]", item)

select_operator: int = int(input("select the operator :- "))

y: int = int(input("Enter second number :- "))


def addition() -> None:
    result: int = x + y
    print("your result is ", result, sep=" ")


def subtraction() -> None:
    result: int = x - y
    print("your result is ", result, sep=" ")


def multiply() -> None:
    result: int = x * y
    print("your result is ", result, sep=" ")


def devision() -> None:
    result: float = float(x / y)
    print("your result is ", result, sep=" ")


def expo() -> None:
    result: int = x**y
    print("your result is ", result, sep=" ")


def sqrt() -> None:
    result: float = math.sqrt(x)
    print("your result is ", result, sep=" ")


if select_operator == 1:
    addition()

elif select_operator == 2:
    subtraction()

elif select_operator == 3:
    multiply()

elif select_operator == 4:
    devision()

elif select_operator == 5:
    expo()

elif select_operator == 6:
    sqrt()

else:
    print("please select the correct operator")
