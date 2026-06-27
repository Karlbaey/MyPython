# Recv a integer bigger than 0 and print res (True if it is leap year, False conversely)
# Author: Karlbaey
def leap(yr: int) -> bool:
    if yr < 1000:
        raise ValueError("Too small! You need to enter a number greater than 1000")
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
        return True
    else:
        return False


yr: int = int(input("Enter the year: "))
try:
    print(f"Is it leap year? {leap(yr)}")
except ValueError as e:
    print(e)
