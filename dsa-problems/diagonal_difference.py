# diagonal difference on Hackerrank
def diagonalDifference(arr):
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - i - 1] for i in range(n))
    return abs(primary - secondary)
if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(diagonalDifference(arr))
