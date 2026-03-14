# Factorial using Function
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  
    return result

print(fact(7))  # Output: 5040


# Check prime number
def prime(n):
    if n <= 1:
        return False   
    for i in range(2, n):
        if n % i == 0:
            return False
    return True       

print(prime(7))  # Output: True


# Find sum of the list 
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

my_list = [1, 2, 3, 4, 5]  
print(list_sum(my_list))    # Output: 15
