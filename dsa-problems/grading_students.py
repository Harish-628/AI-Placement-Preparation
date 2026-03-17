#Grading the students in HackerRank
def gradingStudents(grades):
    rounded = []
    for g in grades:
        if g >= 38:
            next_multiple = ((g // 5) + 1) * 5
            if next_multiple - g < 3:
                g = next_multiple
        rounded.append(g)
    return rounded

if __name__ == '__main__':
    grades_count = int(input().strip())    
    grades = []
    for _ in range(grades_count):
        grades.append(int(input().strip()))
    result = gradingStudents(grades)
    for r in result:
        print(r)
