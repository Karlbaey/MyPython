# Recv a float input (Fahrenheit degree) and print res (°F and Celsius degree).
# Author: Karlbaey

f: float = float(input("Please enter a Fahrenheit degree: "))
c: float = (f - 32) / 1.8
print("%.1f °F == %.1f °C" % (f, c))
print(f"{f:.1f} °F == {c:.1f} °C")  # Equal to previous format
