# completed the breaking the record problem in HackerRank
def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    
    max_count = 0
    min_count = 0
    
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    
    return max_count, min_count


# Input
n = int(input("Enter number of games: "))
scores = list(map(int, input("Enter scores: ").split()))

# Function call
max_breaks, min_breaks = breakingRecords(scores)

# Output
print(max_breaks, min_breaks)
