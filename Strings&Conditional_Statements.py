#String

str1= "this is a string."
str2 = ' Currently studying at NIET'
Str3 = '''This is a string with multiple lines'''

#Basic String Operations

#Concatenation
# "hello" + "world" => "helloworld"
str4 = str1 + str2
print(str4)

#Length of a string
print(len(str1))

#String Indexing
print(str1[0]) #First character
print(str1[5]) #Sixth character
print(str1[-1]) #Last character
print(str1[-5]) #Fifth character from the end

#String Slicing
print(str1[0:4]) #First four characters
print(str1[5:]) #From sixth character to the end
print(str1[:4]) #First four characters
print(str1[-5:]) #Last five characters

#String Functions
print(str1.upper()) #Convert to uppercase
print(str1.lower()) #Convert to lowercase
print(str1.replace("string", "text")) #Replace substring
print(str1.split()) #Split string into a list of words
print(str1.endswith("xt"))#Check if string ends with "xt"
print(str1.startswith("This"))#Check if string starts with "This"
print(str1.capitalize())#Capitalize the first character of the string
print(str1.find("string"))#Find the index of the first occurrence of "string"
print(str1.count("i"))#Count the number of occurrences of "i"


#Write  a program to input user's full name & print its length
a=str(input("Enter your full name: "))
print("Length of your name is:",len(a))


#Write a program to find the occurence of '$' in the string
a=str(input("Enter a string: "))
print("Total number of $ present in the string is:",a.count("$"))



#Conditional Statements

#if-elif-else Statement
"""
if condition:
    # code block
elif condition:
    # code block
else:
    # code block
"""
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


#Nested if Statement
"""
if condition1:
    if condition2:
        # code block
"""
number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("The number is a positive even number.")
    else:
        print("The number is a positive odd number.")


#Write a program to check if a number entered by the user is even or odd
a=float(input("Enter a Number: "))
if( a%2 == 0 ):
    print("Even")
else:
    print("Odd")


#Write a program to find the greatest of 3 number enterd by the user
a=float(input("Enter The First Number: "))
b=float(input("Enter The Second Number: "))
c=float(input("Enter The Third Number: "))
if(c>a and c>b):
    print("The Third Number Is The Greatest")
elif(b>a and b>c):
    print("The Second Number Is The Greatest")
else:
    print("The First Number Is The Greatest")


#Write a program to check if a number is multiple of 7 or not
a=float(input("Enter a Number: "))
if(a%7 == 0):
    print("The Number Is A Multiple Of 7")
else:
    print("The Number Is Not A Multiple Of 7")

    