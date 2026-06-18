# Recv a float (radius of the circle) input and print res (circumference and area).
# Author: Karlbaey

from math import pi

r: float = float(input("Please enter the radius: "))
c: float = 2 * pi * r
a: float = pi * r * r
print(f"The circumference is {c:.2f} and the area is {a:.2f}.")
print(
    f"{c = :.2f} and {a = :.2f}."
)  # Well this does not print the words "circumference" and "area" because the format does not support.
