#Loops

#While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

#Break and Continue Statements
i = 1
while i <= 10:
    if i == 5:
        break#Exits the loop when i is equal to 5
    print(i)
    i += 1

i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue#Skips the rest of the code in the loop when i is equal to 5 and continues with the next iteration
    print(i)
    i += 1


#Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

#Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

#Print the multiplication table of a number n
n = 5
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1



#For Loop
for i in range(1, 6):
    print(i)



#Nested For Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

#Pass Statement
for i in range(1, 6):
    if i == 3:
        pass#Does nothing and continues with the next iteration
    print(i)


#WAP to find the sum of first n numbers( using while loop)
n = 5
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "numbers is:", sum)

#WAP to find the factorial of a number n( using for loop)
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is:", factorial)
