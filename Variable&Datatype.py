#Variable
name = "Shlok"
age = 20
price = 25.9

print(name,age,price)

#Datatype
print(type(name))
print(type(age))
print(type(price))

a=2
b=3
c=a+b
print(c)

#Operators
#Arithmetic Operators

a=10
b=5
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a%b) #Modulus
print(a**b) #Exponentiation
print(a//b) #Floor Division

#Relational/Comparison Operators
print(a==b) #Equal to
print(a!=b) #Not equal to
print(a>b) #Greater than
print(a<b) #Less than
print(a>=b) #Greater than or equal to
print(a<=b) #Less than or equal to

#Assignment Operators
a=10
a+=5 #a=a+5
print(a)
a-=3 #a=a-3
print(a)
a*=2 #a=a*2
print(a)
a/=4 #a=a/4
print(a)
a%=3 #a=a%3
print(a)
a**=2 #a=a**2
print(a)
a//=2 #a=a//2
print(a)

#Logical Operators
x = True
y = False
print(x and y) #Logical AND
print(x or y) #Logical OR
print(not x) #Logical NOT
print(not y) #Logical NOT


#Type Conversion(the conversion is automatic)
a = 2
b = 6.5

sum = a + b
print(sum)

#Type Casting(the conversion is done by the user)
a = 2
b = float("3.5")

sum = a + b#b is converted to an integer
print(sum)



#Input and Output in python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, " + name + "! Welcome to Python programming.")
print("Your age is: " + str(age))



#Writ a Program to input 2 number & print thier sum
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
print("The sum of",a,"and",b,"is:",sum)

#Write a program to input side of a square and print its area
side = float(input("Enter the side of the square: "))
area = side * side
print("The area of the square is:", area)

#Write a program to input 2 floating point numbers and print thier average
num1 = float(input("Enter first floating point number: "))
num2 = float(input("Enter second floating point number: "))
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", average)

#Write a program if a is greater than or eqaul to b. If not print False
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
if a >= b:
    print("True")
else:
    print("False")
