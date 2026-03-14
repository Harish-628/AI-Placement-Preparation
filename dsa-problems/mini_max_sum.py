#Mini max sum HackerRank
def miniMaxSum(arr):
    sum1 = 0
    max1 = arr[0]
    mini = arr[0]
    min1 = 0
    for i in arr:
        sum1 += i
    for i in range(len(arr)):
        if (mini > arr[i]):
            mini = arr[i]
        elif (max1 < arr[i]):
            max1 = arr[i]
    min1 = sum1 - max1
    max1 = sum1 - mini
    print(min1, max1)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
