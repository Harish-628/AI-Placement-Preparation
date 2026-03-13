def compareTriplets(a, b):
    alice = 0
    bob = 0
    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif x < y:
            bob += 1
    return [alice, bob]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*compareTriplets(a, b))
