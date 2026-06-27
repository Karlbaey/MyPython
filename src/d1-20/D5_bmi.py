# Recv two floats (height and weight) and print bmi and analysis
# Author Karlbaey
h: float = float(input("Please enter the height in cm: "))
w: float = float(input("Please enter the weight in kg: "))
h /= 100
bmi: float = w / (h * h)

print(f"Your BMI: {bmi:.2f}.", end=" ")
if bmi < 18.5:
    print("You're too light!")
elif 18.5 <= bmi <= 24:
    print("You have a good build.")
else:
    print("You're too heavy!")
