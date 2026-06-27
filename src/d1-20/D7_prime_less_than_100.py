# Find all prime numbers less than 100
# Author: Karlbaey

for i in range(2, 101):
    is_prime: bool = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)
