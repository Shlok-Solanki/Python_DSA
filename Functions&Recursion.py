#Functions

def greet(name):
    print("Hello, " + name + ". How are you?")
greet("Shlok")#Calling the function with an argument


def add(a, b):
    return a + b
result = add(5, 3)#Calling the function with arguments and storing the return value in a variable
print(result)


#WAF to print the length of a list. (list is the parameter)
def print_length(lst):
    print("Length of the list is:", len(lst))

my_list = [1, 2, 3, 4, 5]
print_length(my_list)

#WAF to print the elements of a list in a single line. (list is the parameter)
def print_elements(lst):
    for element in lst:
        print(element, end=" ")
    print()  # Print a newline at the end

my_list = [1, 2, 3, 4, 5]
print_elements(my_list)

#WAF to find the factorial of a number n. (n is the parameter)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = 5
print("Factorial of", number, "is:", factorial(number))

#WAF to convert USD to INR
def convert_usd_to_inr(usd_amount):
    exchange_rate = 91.66  # Example exchange rate
    return usd_amount * exchange_rate

usd_amount = 100
inr_amount = convert_usd_to_inr(usd_amount)
print(f"{usd_amount} USD is equal to {inr_amount} INR")


#Recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
print("Fibonacci sequence up to", n, "is:")
for i in range(n):
    print(fibonacci(i), end=" ")


#WARF to calculate the sum of first n natural numbers using recursion
def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
n = 5
print("Sum of first", n, "natural numbers is:", sum_of_natural_numbers(n))

#WARF to print all the elements of a list using recursion
def print_elements(lst, index=0):
    if index < len(lst):
        print(lst[index], end=" ")
        print_elements(lst, index + 1)
    else:
        print()  # Print a newline at the end
my_list = [1, 2, 3, 4, 5]
print("Elements of the list are:")
print_elements(my_list)
