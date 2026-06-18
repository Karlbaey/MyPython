# Operators and Formatting

Operators are simply for those arithmetic and boolean logic stuff. They're rather simple so I  won't dwell on them. Formatting, however, plays quite a few tricks.


```python
a: int = 100
b: float = 1.0410133

print(f"integer like {a} and float like {b}.")
print("integer like %d and float like %f." % (a, b)) # Default to six decimal places

# Control decimal places for rounding
print(f"integer like {a} and float like {b:.1f}.")

# str.format() method
print("integer like {} and float like {}.".format(a, b))
```

I would like to memorize these practical ones, as I will look up more usages on Stack Overflow when needed. :)
