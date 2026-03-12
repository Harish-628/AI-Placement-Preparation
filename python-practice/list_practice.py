#sum of the list 
numbers=[2,4,6,8]
total=0
for i in numbers :
  total += i

print("the total sum of the array is " , total)

#Largest Number in list 
numbers=[2,4,5,7,9,8]
largest=numbers[0]
for i in numbers:
  if  largest < i:
    largest = i
    
print(" the largest number in the list is " , largest)

#count even numbers in a list 
numbers=[2,5,7,8,4,6]
count=0
for i in numbers :
  if i%2==0:
   count+=1
print("The total count of the even number is ", count)
