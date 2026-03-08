#File Input and Output in Python

#Opening a file for reading
file = open('example.txt', 'r')
#Reading the contents of the file
content = file.read()
print(content)
#Closing the file
file.close()

#Opening a file for writing
file = open('example.txt', 'w')
#Writing to the file
file.write("Hello, this is an example of file input and output in Python.")
#Closing the file
file.close()

#Opening a file for appending
file = open('example.txt', 'a')
#Appending to the file
file.write("\nThis line is appended to the file.")
#Closing the file
file.close()

