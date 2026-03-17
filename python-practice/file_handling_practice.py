# Write to file 
file=open("sample.txt","w")
file.write("Hello,this is my first file Handling program.")
file.close()

#Read from a file
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

#append to a file
file=open("sample.txt","a")
file.write("\n learning python file handling ")
file.close()
