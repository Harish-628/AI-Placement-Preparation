#completed the kangaroo problem in HackerRank
def kangaroo(x1, v1, x2, v2):
    for _ in range(10000):  # simulate jumps
        if x1 == x2:
            return "YES"
        x1 += v1
        x2 += v2
    return "NO"

# Taking input from user
x1, v1, x2, v2 = map(int, input("Enter x1 v1 x2 v2: ").split())

# Calling function
result = kangaroo(x1, v1, x2, v2)

# Printing result
print(result)
