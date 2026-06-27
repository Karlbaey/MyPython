# print multiplication table
# Author: Karlbaey

# generate a multiplication table
def gen_table(pattern: str = "lb") -> None:
    # Left-bottom
    if pattern == "lb":
        for x in range(1, 10):
            for y in range(1, x + 1):
                print(f"{y}x{x}=={x * y}", end="\t")
            print()

    # Right-bottom
    if pattern == "rb":
        for x in range(1, 10):
            print(f"{(9 - x) * '\t'}", end="")
            for y in range(1, x + 1):
                print(f"{y}x{x}=={x * y}", end="\t")
            print()

    # Left-top
    if pattern == "lt":
        for x in range(1, 10):
            for y in range(1, 11 - x):
                print(f"{x}x{y}=={x * y}", end="\t")
            print()

    # Right-top
    if pattern == "rt":
        for x in range(1, 10):
            print(f"{(x - 1) * '\t'}", end="")
            for y in range(x, 10):
                print(f"{x}x{y}=={x * y}", end="\t")
            print()
    print()


gen_table("lb")
gen_table("rb")
gen_table("lt")
gen_table("rt")
