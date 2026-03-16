#1.Student Marks Dictionary 
student_marks = {
  "Alice":85,
  "Bob":90,
  "Charlie":78
}
print(student_marks["Bob"])

#2.Add item to dictionary 
student_marks={
  "Alice":85,
  "Bob":90
}
student_marks["David"]=88
print(student_marks)

#3.Find the Highest Marks
student_marks = {
  "Alice":85,
  "Bob":90,
  "Charlie":78
}
highest=max(student_marks.values())
print("Highest marks " , highest)
