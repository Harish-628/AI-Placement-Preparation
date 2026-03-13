#Reverse a string
text="Hacker"
reversed_text=text[::-1]
print("The reversed text is :",reversed_text)

#check palindrome 
text="Hacker"
reversed_text=text[::-1]
if (text==reversed_text):
  print("It is palindrome")
else:
  print("It is not")

#Count vowels
text="Hacker"
vowels="aeiouAEIOU"
count=0
for char in text:
  if char in vowels:
    count+=1
print(f"the total numbers of vowels is {count}")    
