#birthday cake candles problem in HackerRank
def birthdayCakeCandles(candles):
    count = 0
    tallest = candles[0]

    # Find the tallest candle
    for i in candles:
        if i > tallest:
            tallest = i

    # Count how many candles have the tallest height
    for i in candles:
        if i == tallest:
            count += 1

    return count


if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    print(birthdayCakeCandles(candles))
