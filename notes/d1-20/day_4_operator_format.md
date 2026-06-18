# 运算符和格式化

运算符就是加减乘除、布尔逻辑之类的玩意，比较简单。

但是格式化倒是有很多写法。

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

记几个常用的得了，以后用到再去 Stack Overflow 上边现查。
