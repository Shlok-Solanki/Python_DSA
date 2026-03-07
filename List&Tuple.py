#List
my_list = [1, 2, 3, 4, 5, "Hello", 3.14, True]
print(my_list) #Print the entire list

#Slicing and Indexing
print(my_list[0]) #Access first element
print(my_list[-1]) #Access last element
print(my_list[2:5]) #Access a slice of the list

#List Functions
my_list.append("World") #Add an element to the end of the list
print(my_list)
my_list.insert(2, "Inserted") #Insert an element at a specific index
print(my_list)
my_list.remove(3) #Remove the first occurrence of an element
print(my_list)
my_list.pop() #Remove and return the last element
print(my_list)

list=[3, 1, 4, 2, 5]
list.sort() #Sort the list (only works if all elements are of the same type)
print(list)
list.reverse() #Reverse the list
print(list)


#Tuple
my_tuple = (1, 2, 3, 4, 5, "Hello", 3.14, True)
print(my_tuple) #Print the entire tuple

#Slicing and Indexing
print(my_tuple[0]) #Access first element
print(my_tuple[-1]) #Access last element
print(my_tuple[2:5]) #Access a slice of the tuple

#Tuple Functions
print(my_tuple.count(3)) #Count the number of occurrences of an element
print(my_tuple.index("Hello")) #Find the index of the first occurrence of an element
print(len(my_tuple)) #Get the length of the tuple


#Write a program to ask the user to enter the names of thier 3 favourite movies & store them in a list
movies = []
for i in range(3):
    movie = input("Enter the name of your favourite movie: ")
    movies.append(movie)
print("Your favourite movies are:", movies)


#Write a program to check if a list contains a palindrome of elements
l1=[1,2,3,4]
copy_l1 = l1.copy()
copy_l1 = l1.reverse()

if(copy_l1 == l1):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Write a program to count the number of students with the "A" grade in the following tuple
grades = ("A", "B", "A", "C", "A", "B", "D")
print("Number of students with grade A:", grades.count("A"))

#Store the above values in a list & sort them from "A" to "D"
grade_list = list(grades)
grade_list.sort()
print("Sorted grades:", grade_list)


