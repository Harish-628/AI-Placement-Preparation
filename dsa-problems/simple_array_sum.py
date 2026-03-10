#problem Sum of array
#platform:hackerRank
#difficulty : easy
def simpleArraySum(ar):
    total = 0
    for i in ar:
        total += i
    return total
ar_count = int(input("Enter number of elements: "))
ar = list(map(int, input("Enter the elements separated by space: ").split()))

result = simpleArraySum(ar)
print("Sum of array elements:", result)
