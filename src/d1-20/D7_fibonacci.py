# Find first 20 numbers of Fibonacci number sequence

a: int = 0
b: int = 1
for _ in range(20):
    a, b = b, a + b
    print(a)
